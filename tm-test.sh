workdir=$(echo $(cat config/config.json | jq ".depolymentpwd")|sed 's/\"//g')
ted_dir=$(echo $(cat config/config.json | jq ".projectpwd")|sed 's/\"//g')
ted_bin=$(echo $(cat config/config.json | jq ".projectbin")|sed 's/\"//g')
container_id=$(echo $(cat config/config.json | jq ".containerid")|sed 's/\"//g')
cd $workdir

# sudo rm -rf sum.log
cmd=$(python3 py/test.py $1 $2 $3 $4 $5)
echo "开始测试"
echo $cmd
# sudo docker exec -i ae9ff934b10b bash -c "$cmd" >> sum.log
echo "完成测试"


tps=$(python3 py/calculate.py)
total=$[$1*$2]
shardtotal=$[$1*$4]
echo $1 $shardtotal $total $tps  >> tps/tps.log


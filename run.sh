

while true;do
current_hour=`date +'%H'`
current_min=`date +'%M'`
echo $current_hour
echo $current_min
if ([ $current_hour -eq 10 ] && [ $current_min -eq 10 ]) || ([ $current_hour -eq 12 ] && [ $current_min -eq 15 ]) || ([ $current_hour -eq 15 ] && [ $current_min -eq 19 ]); then
  git pull
  source venv/bin/activate
  python main.py
  git add index.html
  git commit -m 'added newly generated file for karnataka'
  git push origin
else
  echo Nope
fi
sleep 30
done
#git pull
#source venv/bin/activate
#python main.py
#git add index.html
#git commit -m 'added newly generated file for karnataka'
#git push origin
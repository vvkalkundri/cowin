# cowin

This is a repo that gives you everyday status of vaccine availability

https://apisetu.gov.in/public/api/cowin

The python package listed at https://pypi.org/project/cowin/ is used to get the details of the states and the distric ids in it. 

If you want to run the repository in the local then follow the following steps 

- Fork the repository in your local branch 
- Create a virtualenvironment 
- Install the packages in the virtual environment. 
- Run the following commands .
   ~ pip install -r requirements.txt
   ~ python main.py
- Finally you should see index.html have results of karnataka
- If you want to another state, get the list of states by uncommenting the lines
   # states = cowin.get_states()
    # print(states)
- Run the script again to get the state id of the state you want to generate report for . 
- update the state id in state_ids list and then you must see the result for your state. 

~~ If you need any help drop a email to vvkalkundri@gmail.com I am happy to help . 


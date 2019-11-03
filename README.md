# achievement_first_assessment
This application leverages the github api, to pull all user public
repositories. 

# How To Run 
The application relies on a config.json file. Inside that config.json file
you must specify a github username for the param "git_username" and your own api key 
for "api_key" that is assigned to your github account to authenticate
yourself to access the api resources. 

It is highly recommended to run this application keep all dependencies intact with the main.py file since there are other 
python files inside models/ that main.py needs in order to run, as well as the config.json file.

To run the code make sure you have python 3.5+ installed once you do so, you must have the requests python package installed. To install requests run the command below
	pip install requests 

After requests is installed, to run the code via command line type, run the command 

python main.py - This will kick off the application 
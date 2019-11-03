import os, traceback, requests
from models.config import  Config

def run_list_users(api_token: str, git_user_name: str):
    """
    This function is responsible for hitting the List User Repositories API Endpoint to return the list of public
    repositories accessible to a specfic git hub user account. Read more about the documentation here..
    https://developer.github.com/v3/repos/#list-user-repositories
    :param api_token: Git Hub API token
    :param git_user_name: git hub username
    :return:
    """
    try:

        req = requests.get(f'https://api.github.com/users/{git_user_name}/repos?type=all',
                           headers={'Authorization': f'token {api_token}'})
        response = req.json()
        for data in response:
            print(data['name'])
    except Exception as e:
        print(f'There was an exception raised in run_list_users() - {e}')
        traceback.print_stack()
        os._exit(1)


def main():
    """
    This is the main entry point of the application
    :return:
    """
    conf_obj = Config(config_json_path='config.json')
    conf_obj.load_config_file()
    conf_params = conf_obj.get_config_params()
    run_list_users(api_token=conf_params['api_key'],
                   git_user_name=conf_params['git_username'])




if __name__ == '__main__':
    main()
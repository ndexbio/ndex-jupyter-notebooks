from os.path import isfile, expanduser
import ndex2
import json

def load_tutorial_config(server="public.ndexbio.org"):
    my_username = None
    my_password = None
    my_ndex = None
    config_file = expanduser("~/ndex_tutorial_config.json")
    save_tutorial_networks_to_my_account = True

    if(isfile(config_file)):
        file = open(config_file, "r")
        data = json.load(file)
        file.close()
        if data.get("password") and data.get("username"):
            my_username = data.get("username")
            my_password = data.get("password")
        else:
            print("Error: " + config_file + " does not define username and password")
    else:
        print("Error: " + config_file + " was not found")

        #
    try:
        # Test the connection
        my_ndex=ndex2.client.Ndex2(my_server, my_username, my_password)
        my_ndex.update_status()
        networks = my_ndex.status.get("networkCount")
        users = my_ndex.status.get("userCount")
        groups = my_ndex.status.get("groupCount")
        print("my_ndex client: %s networks, %s users, %s groups" % (networks, users, groups))
        # TODO - check that user can access private account details

    except Exception as inst:
        print("Could not access account %s with password %s" % (my_username, my_password))
        print(inst.args)
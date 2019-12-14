import pysftp
from appJar import gui

app = gui()


def connect_by_sftp():
    ip_host = str(app.getEntry('IP'))
    user_host = str(app.getEntry('Username'))
    password_host = str(app.getEntry('Password'))
    port_host = int(app.getEntry('Port'))

    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  
    with pysftp.Connection(host=ip_host, username=user_host, password=password_host, port=port_host, cnopts=cnopts) as sftp:
        print('Connection succesfully stablished 🔓')

        # Switch to a remote directory
        sftp.cwd('/var/www/alberto-server.ga')

        # Obtain structure of the remote directory '/var/www/vhosts'
        directory_structure = sftp.listdir_attr()

        # Print data
        for attr in directory_structure:
            print(attr)

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        connect_by_sftp()

app.addLabelEntry('IP')
app.addLabelEntry('Username')
app.addLabelSecretEntry('Password')
app.addLabelEntry('Port')

app.addButtons(["Submit", "Cancel"], press)

app.go()


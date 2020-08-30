import os
from os import listdir
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def DriveUpload(post_dir, drive_folder_id, drive_folder_name):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    new_folder = drive.CreateFile({'title':'{}'.format(drive_folder_name),'parents':[{'id': '{}'.format(drive_folder_id)}],'mimeType':'application/vnd.google-apps.folder'}) #Creates a new folder on drive
    new_folder.Upload()
    fnames = listdir(post_dir)
    print(fnames)
    for fname in fnames:
        if (fname.endswith(".jpg") or fname.endswith(".png")):
            print(fname)
            file_path = os.path.join(post_dir, fname)
            nfile = drive.CreateFile({'title':os.path.basename(fname),'parents':[{u'id': new_folder['id']}]})
            nfile.SetContentFile(file_path)
            nfile.Upload()


post_dir = "/home/saurabh/Desktop/Work/Learn To Skill Up/Post Automation/Post7"
drive_folder_id = '1-pU2Tvv3yzPu8CrvKr9khlUDlX0zHjid'
drive_folder_name = 'Post 7'
DriveUpload(post_dir, drive_folder_id, drive_folder_name)
#1-pU2Tvv3yzPu8CrvKr9khlUDlX0zHjid
import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from,file_to):
        """upload a file to Dropbox using API v2
        """

        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from,'rb') as f :
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BDdzH0R4R7wpuylcPYytNZxBH7U4Pv5RNMa551FBh4Y41aIabDL3GxvrBULZA-b2fJSi9JDDJlEkniX-aRr366eo4C9_WB_Gv-uhzkAHhZfnFAasKo6_5MB96AzUGGg3TfmEbo4'
    transferData = TransferData(access_token)

    file_from = './sample1.txt'
    file_to = "/Agamjot Singh Kamboj"

    # Api v2

    transferData.upload_file(file_from,file_to)


main()
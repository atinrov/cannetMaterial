def GzDownload(url,path):
    
    #Libraries
    import urllib.request
    import tarfile
    
    #find URL
    FTPfile = urllib.request.urlopen(url)
    
    #Decompress and save files
    gzfile = tarfile.open(fileobj=FTPfile, mode="r|gz")
    gzfile.extractall(path=path)

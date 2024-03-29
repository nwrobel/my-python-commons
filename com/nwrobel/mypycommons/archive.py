'''
com.nwrobel.archive 

This module contains functionality dealing with archives/compressed files in various formats.
'''

import subprocess
import gzip
import shutil
from com.nwrobel import mypycommons
import com.nwrobel.mypycommons.system
import com.nwrobel.mypycommons.file

class ArchiveSourcePathNotFoundError(Exception):
    '''
    '''
    def __init__(self, message):            
        super().__init__(message)

def extractSingleFileGZArchive(archiveFilepath, outputFilepath):
    '''
    Given the filepath of an input .GZ file and the filepath of the output file, this
    decompresses that single .gz file and creates the decompressed output file.

    This only works for .gz archives that contain single files (a single file is compressed), not 
    for multi-file archives.

    @params
    archiveFilepath: path of the input archive file (gzip)
    outputFilepath: path that will be the output, uncompressed file
    '''
    with gzip.open(archiveFilepath, 'rb') as inputFile:
        with open(outputFilepath, 'wb') as outputFile:
            shutil.copyfileobj(inputFile, outputFile)

def create7zArchive(inputFilePath, archiveOutFilePath, sevenZipCommand=''):
    '''
    Compresses the given paths into a 7zip archive with maximum compression settings.
    
    @params
    inputFilePath: (str or list) the input path(s) to compress into an archive
    archiveOutFilePath: the filepath of the output archive file (should include the .7z extension)
    sevenZipCommand: (optional) string of the command used to execute 7z on this system
    
    @notes
    7zip must be installed on the system and 7z must be in the path for this command to work.
    '''
    if (not isinstance(inputFilePath, list)):
        inputFilePath = [inputFilePath]

    for filePath in inputFilePath:
        if (not mypycommons.file.pathExists(filePath)):
            raise ArchiveSourcePathNotFoundError("The given source path was not found ({}), unable to create archive".format(filePath))

    # Use default 7z executable filepath (differs for Linux and Windows) if one is not specified
    if (not sevenZipCommand):
        if (mypycommons.system.thisMachineIsWindowsOS()):
            sevenZipCommand = 'C:\\Program Files\\7-Zip\\7z.exe'
        else:
            sevenZipCommand = '7z'

    sevenZipArgs = [sevenZipCommand] + ['a', '-t7z', '-mx=7', '-mfb=64', '-md=64m', '-mtc', '-mta', '-mtm', archiveOutFilePath]
    for inFilePath in inputFilePath:
        sevenZipArgs.append(inFilePath)
        
    subprocess.call(sevenZipArgs)

def createTarArchive(inputFilePath, archiveOutFilePath):
    '''
    Compresses the given paths into a TAR archive. This function only works on Linux machines.
    
    @params
    inputFilePath: (str or list) the input path(s) to compress into an archive
    archiveOutFilePath: the filepath of the output archive file (should include the .tar extension)
    '''
    if (not isinstance(inputFilePath, list)):
        inputFilePath = [inputFilePath]

    for filePath in inputFilePath:
        if (not mypycommons.file.pathExists(filePath)):
            raise ArchiveSourcePathNotFoundError("The given source path was not found ({}), unable to create archive".format(filePath))

    if (mypycommons.system.thisMachineIsWindowsOS()):
        raise Exception("createTarArchive function is not supported on Windows machines (only works on Linux-type machines)")

    tarArgs = ['tar', 'cvf', archiveOutFilePath]
    for inFilePath in inputFilePath:
        tarArgs.append(inFilePath)
        
    subprocess.call(tarArgs)
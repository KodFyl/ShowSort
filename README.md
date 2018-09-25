
# ShowSort

ShowSort is custom-made tool for TV Shows lovers. The video files of different shows are sometimes scattered in a folder. Arranging each files to their respective Shows, Season manually is difficult, time consuming and boring task. That's where the ShowSort tool comes handy. ShowSort tool accepts a pattern that is used to identify the files in given directory and moves the identified files to new directory. During the process, the ShowSort tool classifies the files into the order: "Show/Season/Episode". Therefore, your library of TV Shows will look neat and well arranged. Thus, navigating within your Show library is made hassle-free.


Instructions for running:

1. Open master directory in terminal.
2. Give executable permission by command: "chmod +x ShowSort.py".
3. Run with "./ShowSort.py".


Intructions for freezing:

Following instructions are using python module 'PyInstaller' on Ubuntu platform. You may use other modules to freeze depending upon the target platform.

1. Install pip for Python3 if not already installed. In Debian/Ubuntu, use command: "sudo apt install python3-pip".
2. Using pip, install package 'PyInstaller'. Use command: "pip3 install PyInstaller".
3. To freeze, use command: "python3 -m PyInstaller ShowSort.py --onefile"
4. The executable can be found in 'dist' directory. 


For licensing information, see 'LICENCE'.


Warning: This is a Beta release. Bugs are expected. if any comes in your way, let the author know at the e-mail provided. Feedback & Suggestions are also welcomed.

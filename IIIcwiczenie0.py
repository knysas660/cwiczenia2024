# aby utworzyć zmienną środowiskową i ustanowić ją w pliku .profile należy wpisać w nim:

export oraz zmienną np. export x=100 następnie w wierszu poleceń zainstalować wpisując:
source .profile

# inny przykład to wpisanie ścieżki programu w zmiennej PATH:

export PATH=$PATH:/home/osboxes/jdk-15.0.2/bin

# następny przykład z cwiczenia zmienna python_projects wpisaną w .profile:

export python_projects=/home/kaliluk/Python/cwiczenia/

# następnie wpisać w powloce: source .profile potem $python_projects lub cd $python_projects


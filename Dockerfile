FROM debian
RUN apt update;\
    apt install -y python3;\
    apt install -y pip;\
    pip install numpy;\
#docker build -t conda_bien . hau ipini behar da irudia sortzeko (ointxe sortuta dago jada)
#Aldatu docker-eko konfigurazioa baimena emateko bolumenak partekatzean
#docker images ikusteko irudiak
#docker run -rm -it -v /System/Volumes/Data/sgoinfre/goinfre/Perso/ubegona/AI_bootcamp:/home/nahi_duzun_karpeta irudiaren_izena (rm-rekin borratu egiten da ateratzerakoan)
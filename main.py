from pytube import YouTube

try:
    with open("list.txt", "r") as f:
        for link in f.readlines():
            yt = YouTube(link)
            my_stream = yt.streams.filter(res="1080p").first()
            print(my_stream)
            key = input("Inserisci il tag della stream desiderata per scaricarla: ")
            try:
                yt.streams.get_by_itag(int(key))\
                .download(
                    output_path=".",
                    filename=str(my_stream.title)
                )
            except:
                print("Errore nel download della stream selezionata. Prova con un nuovo link o un'altra stream")
except:
    print("Errore durante la lettura della lista dei link, per favore riprova o contatta ciccio sbengh")
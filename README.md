# CassaCriptata
Il programma CassaCriptata è una cassaforte che usa l'algoritmo GC57 a difesa dei nostri dati.
Come funziona: Innanzi tutto dovremo creare una chiave con il programma TestCampo il quale ci fornirà un file dati che verrà memorizzato su di una chiavetta USB.
I dati di questo file son importantissimi, in quanto la loro perdita significherebbe non riuscire più a decodificare i nostri file. Per questo motivo devono essere tunuti al sicuro
in una copia lontano dal computer. Questo metodo di tenere i dati sulla chiavetta è per fornire al programma una doppia serratura. La prima serratura è la password che dovrà essere bella robusta, e la seconda serratura
sarà appunto la chiavetta, che senza di essa i dati non potranno essere decifrati.
La scelta della grandezza in Bit, come spiegato nel programma TestCampo, dipende dalla nostra necessità di protezione. Naturalmente con più saranno alti questi Bit, con più avremo un codice inviolabile.
All'inizio il programma, dopo aver chiesto la password, chiederà di indicare la porta USB se diversa da quella impostata di default e cioè "D".
I dati memorizzati invece, sono all'interno del programma, impostati su "C:\DCP\dropbox". Perchè questo indirizzo? Innanzi tutto lo potete cambiare come volete ma una volta compilato il programma non si potrà più cambiare. 
Per quanto mi riguarda l'ho impostato così perchè su qualsiasi computer io usi ho la possibilità di leggere i file memorizzati e poi perchè avere un cloud tipo dropbox mi garantisce che se il mio computer si bloccasse, per un qualsiasi motivo,
o qualcuno cancellasse i miei file, li potrei sempre recuperare da dropbox. Naturalmente di cloud ce ne sono altri e vi basterà mettere il vostro.
Nel caso il programma venisse cancellato o hakerato, con i dati della chiavetta riuscirete comunque a recuperare tutti i vostri file. Questo naturalmente utilizzando un altro programma non ancora compilato e tenuto in un luogo sicuro.

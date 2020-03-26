#### pooledParser.py
A simple scraping script for proteinatlas.org for extracting IF images whenever they exist, given a list input. Program takes advantage of multiprocessing's Pool feature, so N-1 CPU core's amount of processes may run concurrrently.

\
Dependencies are python3, requests and lxml.
```
git clone ttps://github.com/spmoran/pooledParser.git
chmod 755 pooledParser.py

pooledParser.py INPUT
```

Input is like:\
SNRPA1 	 P09661\
SETD2 	 A0A1W2PPX9\
PTPN23 	 Q9H3S7\
\
Where enties are GeneID and UniProt# delimited by tab. Order does not matter. ENSG ID is also recognized by proteinaltas.org. Output files are the images in the format 
{COL1}-{COL2}<htmlimagepath>.jpg
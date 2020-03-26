#### pooledParser.py



TODO: fix directory inputs/fileoutputs. Currently can only be run by placing file inputs in directory with pooledParser.py

A suite of scripts for rapidly assessing protein disorder and examining availible images. Command Chomp chunks data for better function, command get retrieves disordered protein information, and command scrape retrieves any available IF images from proteinatlas.org
 

```
git clone https://github.com/spmoran/pooledParser.git
pip install -r ./pooledParser/requirements.txt
chmod 755 ./pooledParser/pooledParser.py

```
\
There are three major commands:
1. get
2. chomp
3. scrape

####get:
```
pooledparser --command get --i "./pathwaydirectory"

Input: output of the chomp command, or input should be a JQ_(N-1)Kto(N)K.txt file, where a list of UNIPROT ids.
Out: JQ_OUT.txt should be table of outputs with:

--------------------------------------------------------------------
|UniProt|GeneName|Gene Length|Disordered Domains|Percent Disordered|
--------------------------------------------------------------------
Intermediate files (1K each) also included in case of breakage.
```

####chomp:
```
pooledparser --command chomp --i "filename"

Input: List of Uniprot ID's.
Output: Many files of line length 1K, chunked from input. This will be formatted for the get function.

```

####scrape:
```
pooledparser --command scrape --i "filename"

Input: textfile with lines such as GeneID + \t + UniProtID. Using ENSG instead of GeneName is also okay. Something like this:
SNRPA1 	 P09661
SETD2 	 A0A1W2PPX9
PTPN23 	 Q9H3S7

Output: all IF images availible for entry on proteinatlas.org. Several other photos are not accessible this way (need JQuery to server), so proteins of interest should still be checked manually. All are in format: {COL1}-{COL2}<htmlimagepath>.jpg
```

#! /usr/bin/env python3

import requests
import pandas as pd
# from pandas import json
import json
from getdir import PercentDisordered

def json_get(lookup_url, urlsession):
    OUT = list()
    if lookup_url:
        # print("TRUE")
        OUT.append(lookup_url)
        try:
            uniprot_var = urlsession.get("https://mobidb.bio.unipd.it/ws/{}/uniprot".format(lookup_url)).json()
            OUT.append(uniprot_var['name'])
            OUT.append(uniprot_var['gene'])
            OUT.append(uniprot_var['sequence'])
            OUT.append(uniprot_var['length'])
        except KeyError:
            return 0
        except urlsession.Timeout as err:
            logger.error({"message": err.message})
        except session.RequestException as err:
            logger.error('there was an issue with {}'.format(lookup_url))
        except json.decoder.JSONDecodeError:
            return 0

        try:
            consensus_var = urlsession.get("https://mobidb.bio.unipd.it/ws/{}/consensus".format(lookup_url)).json()['mobidb_consensus']['disorder']['predictors']
            for X in consensus_var:
                # print("interating {}".format(X))
                if 'mobidb_lite' in X.values():
                    OUT.append(X['regions'])
                else:
                    pass
        except KeyError:
            return 0

        except urlsession.Timeout as err:
            logger.error({"message": err.message})
        except urlsession.RequestException as err:
            logger.error('there was an issue with {}'.format(lookup_url))
        except json.decoder.JSONDecodeError:
            return 0
        OUT.append(PercentDisordered.PCN_disordered(OUT[4],OUT[5]))
        return OUT
    else:
        return 0

def call_and_write(in_file_name):
    # yoinks = sys.argv[1]
    yoinks = in_file_name
    print('called call_and_write')
    write_to_pandas = list()
    with open(yoinks, "r+") as infile:
        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=3000,pool_maxsize=3000)
        session.mount('https://', adapter)
        RETURN = list()
        for X in infile:
            #something here
            inline=json_get(X.rstrip('\n'), session)
            # print(inline)
            if inline:
                RETURN.append(inline)
            if not len(RETURN)%200:
                # for X in RETURN:
                #     print(X)
                write_to_pandas.extend(RETURN)
                RETURN = list()
        if RETURN:
            write_to_pandas.extend(RETURN)
    #print(write_to_pandas)
    pd.DataFrame(write_to_pandas).to_csv(''.join([in_file_name[:-4],'.OUTPUT.txt']), header=None, index=None, sep='\t', mode='a')
    #pd.DataFrame(write_to_pandas).to_excel(''.join([in_file_name[:-4],'.xlsx']), header=False, index=False)
    # for X in RETURN:
    #     print(X)

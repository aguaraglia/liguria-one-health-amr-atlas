import json,requests,time,re,os
R=json.load(open('raw/pubmed_records.json'))
ids=open('ft_ids.txt').read().split()
st={}
GEO=re.compile(r'Liguria|Ligurian|Genoa|Genova|La Spezia|Savona|Imperia|San ?Remo|Chiavari|Rapallo|Lavagna|Sestri|Albenga|Pietra Ligure|Ventimiglia|Gaslini|Galliera|San Martino|Sarzana|Piedmont|Piemonte|Turin|Torino|Valle d.Aosta|Aosta',re.I)
for p in ids:
    r=R[p]; pmc=r.get('pmc','')
    txt=None; how=''
    if pmc:
        u=f'https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/fullTextXML'
        try:
            x=requests.get(u,timeout=60)
            if x.status_code==200 and len(x.text)>2000:
                open(f'ft/{p}.xml','w').write(x.text); txt=re.sub(r'<[^>]+>',' ',x.text); how=f'EPMC {pmc}'
            else: how=f'EPMC {pmc} HTTP {x.status_code}'
        except Exception as e: how=f'EPMC err {e}'
    else: how='no PMCID'
    snips=[]
    if txt:
        # drop affiliations/refs roughly
        body=txt
        cut=body.find(' References ')
        for m in GEO.finditer(body):
            snips.append(body[max(0,m.start()-140):m.end()+100].replace('\n',' '))
    st[p]=dict(how=how,n=len(snips),snips=snips[:12])
    print(p,how,len(snips)); time.sleep(0.3)
json.dump(st,open('ft/status.json','w'),ensure_ascii=False,indent=1)

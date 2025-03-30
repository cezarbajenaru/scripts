import csv

hosts = [["workstation.local", "192.168.25.46"], ["websserver.cloud", "10.2.5.6"]]
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)




import csv

ip = ["192.168.10.15", "192.165.18.2", "192.178.66.5"]
with open("generate.csv", "w") as generator:
    writer = csv.writer(generator)
    writer.writerows(ip)

    

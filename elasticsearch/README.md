# Elasticsearch for elite-kafka

## Set vm.max_map_count or elasticsearch will fail

In /etc/sysctl.conf set the following line:
````
vm.max_map_count=262144
````

Apply settings for live system
````
sysctl -w vm.max_map_count=262144
````

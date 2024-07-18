<div align="center">
  
# High Level Design Diagram
   <img alt="Demo" src="https://github.com/Sohoxic/PES2UG21CS505-PES2UG21CS532-PES2UG21CS542-PES2UG21CS546-Building-a-distributed-k-v-store-with-etcd/blob/main/Assets/HLD/hld2.png" style="max-width: 100%; height: auto;" />
   
> Components of the distributed k-v store
>   <img alt="Demo" src="https://github.com/Sohoxic/PES2UG21CS505-PES2UG21CS532-PES2UG21CS542-PES2UG21CS546-Building-a-distributed-k-v-store-with-etcd/blob/main/Assets/HLD/hld1.png" style="max-width: 100%; height: auto;" />

</div>


# Week1: Setting Up and Understanding etcd
## Todo
- [X] etcd Installation
- [X] Single-Node Cluster Setup Guide
- [X] Write functions to List all keys using etcd client library.
- [X] Get the value for a specific key provided by the user.
- [X] Put a key-value pair into etcd, allowing users to specify both key
and value.

This guide provides a comprehensive overview of installing etcd, configuring your system to run it, and setting up a single-node etcd cluster on a Linux system.

## Downloading etcd

To download a specific version of etcd from the official GitHub repository:

1. Identify the version you want to download from [etcd releases](https://github.com/etcd-io/etcd/releases/).
2. Use the following commands to download and extract etcd to a temporary location:

```sh
ETCD_VER=<version> # Example: v3.4.31
DOWNLOAD_URL=https://github.com/etcd-io/etcd/releases/download
curl -L ${DOWNLOAD_URL}/${ETCD_VER}/etcd-${ETCD_VER}-linux-amd64.tar.gz -o /tmp/etcd-${ETCD_VER}-linux-amd64.tar.gz
tar xzvf /tmp/etcd-${ETCD_VER}-linux-amd64.tar.gz -C /tmp/etcd-download-test --strip-components=1
```

<div align="center">

> This is how it should appear by the end of installation:

  <img alt="Demo" src="https://github.com/Sohoxic/PES2UG21CS505-PES2UG21CS532-PES2UG21CS542-PES2UG21CS546-Building-a-distributed-k-v-store-with-etcd/blob/main/Assets/week1/installation.png" style="max-width: 100%; height: auto;" />

</div>

## Making etcd Accessible System-wide

After downloading and extracting etcd, you may encounter a message indicating `etcd` command is not found. This is because the binary is not in your system's `PATH`. To resolve this:

### Moving etcd Binaries

1. Move `etcd` and `etcdctl` to a more permanent location, `/usr/local/bin`:

```sh
sudo mv /tmp/etcd-download-test/etcd /usr/local/bin/
sudo mv /tmp/etcd-download-test/etcdctl /usr/local/bin/
```

### Updating the PATH Variable

For bash users, add `/usr/local/bin` to your `PATH` by editing `~/.bashrc`:

```sh
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

For zsh users, modify `~/.zshrc` instead:

```sh
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## Setting Up a Single-Node Cluster

Follow the steps outlined in the etcd documentation for setting up a single-node cluster:

1. Start the etcd server:

```sh
etcd
```

2. Interact with etcd using `etcdctl`:

```sh
etcdctl put mykey myvalue
etcdctl get mykey
```

<div align="center">

> Getting and Setting K-V pair in local system:

  <img alt="Demo" src="https://github.com/Sohoxic/PES2UG21CS505-PES2UG21CS532-PES2UG21CS542-PES2UG21CS546-Building-a-distributed-k-v-store-with-etcd/blob/main/Assets/week1/RetrievingKVpair.png" style="max-width: 100%; height: auto;" />

</div>
<br/>

For detailed instructions, refer to the [etcd Quickstart Guide](https://etcd.io/docs/v3.5/quickstart/).

## Running the `script.py`

To run the `script.py` file and interact with the etcd cluster, perform the following steps:

- [X] Ensure the `etcd` service is running.
- [X] Install the `etcd3` Python package if not already installed:

```
  pip install etcd3
```
 > If you encounter errors related to the protobuf library, downgrade the protobuf package to version 3.20.x or lower:
> ```
> pip install protobuf==3.20.0
> ```
 > or you can set the protocol buffers env. variable:
> ```
> set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
> ```

- [X] Run script.py
```
python script.py
```

<div align="center">

> Output:

  <img alt="Demo" src="https://github.com/Sohoxic/PES2UG21CS505-PES2UG21CS532-PES2UG21CS542-PES2UG21CS546-Building-a-distributed-k-v-store-with-etcd/blob/main/Assets/week1/python1.png" style="max-width: 100%; height: auto;" />

</div>
<br/>


# Week2: Adding Features and Error Handling
## Todo
- [X] Write function to delete keys.
- [x] Write function to implement range scan.
- [X] Error handling for the functions
- [X] Design a CLI.

Run script.py
```
python script.py
```


<div align="center">

> CLI:

  <img alt="Demo" src="https://github.com/Sohoxic/PES2UG21CS505-PES2UG21CS532-PES2UG21CS542-PES2UG21CS546-Building-a-distributed-k-v-store-with-etcd/blob/main/Assets/week2/run-week2.png" style="max-width: 100%; height: auto;" />

</div>
<br/>

# Week3: Testing
## Todo
- [X] Write unit tests for program's functionalities
- [X] Multi-Node cluster set up 

Run script.py
```
python script.py
```


<div align="center">

> Running Unit Tests

  <img alt="Demo" src="https://github.com/Sohoxic/PES2UG21CS505-PES2UG21CS532-PES2UG21CS542-PES2UG21CS546-Building-a-distributed-k-v-store-with-etcd/blob/main/Assets/week3/run-week3.png" style="max-width: 100%; height: auto;" />

</div>
<br/>

<div align="center">

> Multi Node Cluster Setup Running.

  <img alt="Demo" src="https://github.com/Sohoxic/PES2UG21CS505-PES2UG21CS532-PES2UG21CS542-PES2UG21CS546-Building-a-distributed-k-v-store-with-etcd/blob/main/Assets/week3/multiple_nodes_running.png" style="max-width: 100%; height: auto;" />

</div>

<div align="center">

> Multi Node Cluster Before Deleting Leader.

  <img alt="Demo" src="https://github.com/Sohoxic/PES2UG21CS505-PES2UG21CS532-PES2UG21CS542-PES2UG21CS546-Building-a-distributed-k-v-store-with-etcd/blob/main/Assets/week3/before_deleting_leader.png" style="max-width: 100%; height: auto;" />

</div>

<div align="center">

> Multi Node Cluster After Deleting Leader.

  <img alt="Demo" src="https://github.com/Sohoxic/PES2UG21CS505-PES2UG21CS532-PES2UG21CS542-PES2UG21CS546-Building-a-distributed-k-v-store-with-etcd/blob/main/Assets/week3/after_deleating_leader.png" style="max-width: 100%; height: auto;" />

</div>
<br/>

## Note

- This guide focuses on development and testing environments. For production setups, consult the official etcd documentation for security, clustering, and configuration best practices.

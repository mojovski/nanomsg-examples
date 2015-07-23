# Python

## Install

```
git clone https://github.com/tonysimpson/nanomsg-python.git
cd nanomsg-python
python setup.py build
```
if everything is fine:
```
sudo python setup.py install
```

There is an issue with the updates on the libraries in Ubuntu.
You can verify this by calling
```
echo $LD_LIBRARY_PATH 
```
which must not be empty. 
If so, call
```
export LD_LIBRARY_PATH=/usr/local/lib
```
or
```
sudo ldconfig
```
to fix this.


## 

## C module


1. compile: 

```
make
```


2. run the sending instance:
```
./pair tcp://127.0.0.1:49234 
```
or for shared memory transmission:
```
./pair ipc:///tmp/pipeline.ipc
```

3. run the listening python example
```
python listener.py ipc:///tmp/pipeline.ipc
```


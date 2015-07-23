# Python

## Install

git clone https://github.com/tonysimpson/nanomsg-python.git
cd nanomsg-python
python setup.py build
if everything is fine:
sudo python setup.py install
echo $LD_LIBRARY_PATH must not be empty. call
export LD_LIBRARY_PATH=/usr/local/lib
or
sudo ldconfig


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
or 
```
./pair ipc:///tmp/pipeline.ipc
```

3. run the listening python example
```
python listener.py
```


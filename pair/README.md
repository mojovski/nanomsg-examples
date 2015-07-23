#---------
# Python
#--------

## Install

git clone https://github.com/tonysimpson/nanomsg-python.git
cd nanomsg-python
python setup.py build
if everything is fine:
sudo python setup.py install

## 

#------------
# C code
#-----------


1. compile: make

2. run the listening instance:
./pipeline node0 ipc:///tmp/pipeline.ipc & node0=$! && sleep 1

3. run the sending instance
./pipeline node1 ipc:///tmp/pipeline.ipc "Hello, World!"
or once more
./pipeline node1 ipc:///tmp/pipeline.ipc "Some other message"

4. kill the listening instance
kill $node0 

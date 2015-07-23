#include <assert.h>
// see http://stackoverflow.com/questions/21768542/libc-h-no-such-file-or-directory-when-compiling-nanomsg-pipeline-sample
#include <unistd.h>
#include <string>
#include <pthread.h>

#include <stdio.h>
#include <stdlib.h>
#include <nanomsg/nn.h>
#include <nanomsg/pair.h>
#include <iostream>


//creates a node and sends data to it.
int node0 (const char *url)
{
  int sock = nn_socket (AF_SP, NN_PAIR);
  assert (sock >= 0);
  assert (nn_bind (sock, url) >= 0);
  int counter=0;
  while (1)
    {
      std::string txt="counter: "+std::to_string(counter);
      printf ("SENDING \"%s\"\n", txt.c_str());
      int sz_n = txt.size()+1;// '\0' too
      return nn_send (sock, txt.c_str(), sz_n, 0);
      sleep(1);
      counter+=1;
    }
}


int main (const int argc, const char **argv)
{
  if (argc<2)
    {
      std::cerr << "You need to pass at least the address\n";
      return 1;
    }
  else if (argc==2)
  {
    return node0(argv[1]);
  }
  else
  {
    fprintf (stderr, "Usage: pair <URL>\n");
    return 1;
  }
}

CC		= gcc
CXX		= g++
LINK		= g++

NTLPREFIX	= /usr/local
NTLLIB		= -L$(NTLPREFIX)/lib -lntl -lgmp
NTLINCLUDE	= -I$(NTLPREFIX)/include

PREFFLAGS	= -O2 -Wall -I.
CXXFLAGS	= $(PREFFLAGS) $(NTLINCLUDE)
LINKFLAGS	= $(NTLLIB)

ALL_PROGS	= dlog-test
COMMON_OBJS	= vector.o ZZFactoring.o \
		  mat_long.o svector.o smatrix.o SGauss.o \
		  FactorBase.o DiscreteLog.o DLog_IC_Base.o \
		  IndexCalculus.o
COMMON_HEADERS	=


all:	$(ALL_PROGS)

dlog-test:	$(COMMON_OBJS) dlog-test.o
	$(LINK) -o $@ $^ $(LINKFLAGS)

clean:
	rm -f *% *~ *.o core a.out $(ALL_PROGS)


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-8-b85dbb56d4fa>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-8-b85dbb56d4fa>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    *(Assume, 2, is, a, prime, number, but, 0, and, 1, are, not, */)\u001b[0m\n\u001b[1;37m                  ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "/* Assume 2 is a prime number but 0 and 1 are not */\n",
    "void main()\n",
    "{\n",
    "int  i , n , p , d , flag ;\n",
    "  printf(\"Enter n: \") ;\n",
    "  scanf(\"%d\",&n) ;\n",
    "  printf(\"First %d prime numbers are as follows: \\n\",n) ;\n",
    "  p=2;\n",
    "  i=1; \n",
    "while(i<=n)\n",
    "  {\n",
    "    flag=1;\n",
    "for(d=2 ; d<=p-1 ; d++)   /* d<=p/2 is also correct */\n",
    "if(p%d==0)     /* True if number is not prime */\n",
    "      {\n",
    "    flag=0 ;\n",
    "\n",
    "        break ;    /* Loop terminates if p is not prime  */\n",
    "      }  \n",
    "if(flag==1)\n",
    "    {\n",
    "       printf(\"%d \",p) ;\n",
    "   i++ ;\n",
    "    }\n",
    "    p++ ;\n",
    "  }\n",
    "}"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

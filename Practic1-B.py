{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = float(input(\"give me the value of x: \"))\n",
    "\n",
    "if x < -100:\n",
    "    result = -x\n",
    "elif x >= -100 and x <= -25:\n",
    "    result = x ** 4\n",
    "elif x > -25 and x <=100:\n",
    "    result = 3.14/2 *x+3 ** x\n",
    "else:\n",
    "    result = x\n",
    "    \n",
    "print(result)"
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

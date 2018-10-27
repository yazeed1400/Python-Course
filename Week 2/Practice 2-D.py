{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Amman', 'Zarqa', 'Irbid']"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> names = ['Amman', 'Zarqa', 'Irbid', 'Aqaba', 'al-Balqa', 'Madaba']\n",
    ">>> first_letters = ['A','B','C']\n",
    ">>> output_names = [name for name in names if (name[0] in first_letters)]\n",
    ">>> output_names\n",
    "['Amman', 'Zarqa', 'Irbid']"
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

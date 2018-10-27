{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"currency Exchange\")\n",
    "ex= str(input(\"A- Jordanin Dinars to Dollars B-Dollar to Jordanin Dinars C- Jordanin Dinars to Turkish Lira D- Turkish Lira to Jordanin Dinars E- Turkish Lira toDollars G- Dollars to Turkish Lira : \"))\n",
    "if ex== \"A\":\n",
    "    ptd= float(input(\"HOW MUCH WOULD YOU LIKE TO CONVERT: \"))\n",
    "    f= ptd*1.4084\n",
    "    f2= round(f,2)\n",
    "    print(\"it is usd \",f2)\n",
    "if ex== \"B\":\n",
    "    ptd= float(input(\"HOW MUCH WOULD YOU LIKE TO CONVERT: \"))\n",
    "    f= ptd*.710\n",
    "    f2= round(f,2)\n",
    "    print(\"it is JOD \",f2)\n",
    "if ex== \"C\":\n",
    "    ptd= float(input(\"HOW MUCH WOULD YOU LIKE TO CONVERT: \"))\n",
    "    C= ptd*.12\n",
    "    C2= round(f,2)\n",
    "    print(\"it is TRY \",f2)\n",
    "if ex== \"D\":\n",
    "    ptd= float(input(\"HOW MUCH WOULD YOU LIKE TO CONVERT: \"))\n",
    "    C= ptd*8.06\n",
    "    C2= round(f,2)\n",
    "    print(\"it is JOR \",f2)\n",
    "if ex== \"E\":\n",
    "    ptd= float(input(\"HOW MUCH WOULD YOU LIKE TO CONVERT: \"))\n",
    "    E= ptd*5.70\n",
    "    E2= round(f,2)\n",
    "    print(\"it is usd \",f2)\n",
    "if ex== \"G\":\n",
    "    ptd= float(input(\"HOW MUCH WOULD YOU LIKE TO CONVERT: \"))\n",
    "    E= ptd*.175\n",
    "    E2= round(f,2)\n",
    "    print(\"it is TRY \",f2)"
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

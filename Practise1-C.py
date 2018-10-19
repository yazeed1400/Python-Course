{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "temp = input(\"Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : \")\n",
    "degree = int(temp[:-1])\n",
    "i_convention = temp[-1]\n",
    "\n",
    "if i_convention.upper() == \"C\":\n",
    "  result = int(round((9 * degree) / 5 + 32))\n",
    "  o_convention = \"Fahrenheit\"\n",
    "elif i_convention.upper() == \"F\":\n",
    "  result = int(round((degree - 32) * 5 / 9))\n",
    "  o_convention = \"Celsius\"\n",
    "else:\n",
    "  print(\"Input proper convention.\")\n",
    "  quit()\n",
    "print(\"The temperature in\", o_convention, \"is\", result, \"degrees.\")\n"
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

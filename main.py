{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "time: 0.015625\n",
      "\n",
      "3 1 5 | 9 8 4 | 2 7 6 \n",
      "7 2 6 | 5 1 3 | 4 8 9 \n",
      "8 4 9 | 6 7 2 | 1 5 3 \n",
      "---------------------\n",
      "4 6 2 | 3 5 9 | 8 1 7 \n",
      "5 7 8 | 2 6 1 | 3 9 4 \n",
      "1 9 3 | 7 4 8 | 6 2 5 \n",
      "---------------------\n",
      "2 3 1 | 4 9 7 | 5 6 8 \n",
      "6 8 7 | 1 3 5 | 9 4 2 \n",
      "9 5 4 | 8 2 6 | 7 3 1 \n",
      "\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import time\n",
    "\n",
    "def sudoku():\n",
    "    for i in range(100):\n",
    "        try:\n",
    "            data = {}\n",
    "\n",
    "            for i in range(81):\n",
    "                data[i]={'index':i,\n",
    "                         'col':i%9,\n",
    "                         'row':i//9,\n",
    "                         'value':0,\n",
    "                         'box':i//3 - 3*(i//9 - (i//9)//3),\n",
    "                         'pos':[1,2,3,4,5,6,7,8,9],\n",
    "                         'state':'ready'}\n",
    "\n",
    "\n",
    "            def removeOther(r,c,b,n):\n",
    "                for i in range(81):\n",
    "                    if (len(data[i]['pos']) > 0) and (n in data[i]['pos']):\n",
    "                        if(data[i]['row']==r) or (data[i]['col']==c) or (data[i]['box']==b):\n",
    "                            data[i]['pos'].remove(n)\n",
    "\n",
    "            def check():\n",
    "                for i in range(81):\n",
    "                    if (len(data[i]['pos']) < 2) and (len(data[i]['pos']) > 0) and (data[i]['state'] == 'ready'):\n",
    "                        data[i]['value']=random.choice(data[i]['pos'])\n",
    "                        data[i]['state']='checked'\n",
    "                        removeOther(data[i]['row'], data[i]['col'], data[i]['box'], data[i]['value'])\n",
    "\n",
    "\n",
    "            for i in range(81):\n",
    "                if data[i]['state'] == 'ready':\n",
    "                    data[i]['value']=random.choice(data[i]['pos'])\n",
    "                    data[i]['state']='checked'\n",
    "                    removeOther(data[i]['row'], data[i]['col'], data[i]['box'], data[i]['value'])\n",
    "                    check()\n",
    "\n",
    "            break\n",
    "\n",
    "        except:\n",
    "            pass\n",
    "\n",
    "\n",
    "        \n",
    "start = time.process_time()\n",
    "sudoku()\n",
    "end=(time.process_time() - start)\n",
    "print(f\"\\ntime: {end}\\n\")\n",
    "    \n",
    "\n",
    "def draw(text):\n",
    "    demo=''\n",
    "    m=0\n",
    "    for r in range(9):\n",
    "        for n in range(9):\n",
    "            m=f\"{str(data[n+9*r][text])}\"\n",
    "            if n%3==2 and n%9!=8:\n",
    "                demo += m+\" | \"\n",
    "            else:\n",
    "                demo += m+\" \"\n",
    "\n",
    "        demo += \"\\n\"\n",
    "        if r%3==2 and r%9!=8:\n",
    "            demo += \"---------------------\\n\"\n",
    "\n",
    "    return print(demo)\n",
    "\n",
    "draw('value')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Columns:\n",
      "Column 0 is fine\n",
      "Column 1 is fine\n",
      "Column 2 is fine\n",
      "Column 3 is fine\n",
      "Column 4 is fine\n",
      "Column 5 is fine\n",
      "Column 6 is fine\n",
      "Column 7 is fine\n",
      "Column 8 is fine\n",
      "\n",
      "Rows:\n",
      "Row 0 is fine\n",
      "Row 1 is fine\n",
      "Row 2 is fine\n",
      "Row 3 is fine\n",
      "Row 4 is fine\n",
      "Row 5 is fine\n",
      "Row 6 is fine\n",
      "Row 7 is fine\n",
      "Row 8 is fine\n",
      "\n",
      "Boxes:\n",
      "Box 0 is fine\n",
      "Box 1 is fine\n",
      "Box 2 is fine\n",
      "Box 3 is fine\n",
      "Box 4 is fine\n",
      "Box 5 is fine\n",
      "Box 6 is fine\n",
      "Box 7 is fine\n",
      "Box 8 is fine\n"
     ]
    }
   ],
   "source": [
    "def superCheck():\n",
    "    print(f\"Columns:\")\n",
    "    for i in range(9):\n",
    "        s=set()\n",
    "        t=0\n",
    "        \n",
    "        for j in range(9):\n",
    "            n=data[i+t]['index']\n",
    "            s.add(n)\n",
    "            t+=9\n",
    "    \n",
    "        if(len(s)<9):\n",
    "            print(f\"There is a problem with a column {i}\")\n",
    "        else:\n",
    "            print(f\"Column {i} is fine\")\n",
    "    \n",
    "    \n",
    "    print(f\"\\nRows:\")\n",
    "    for i in range(9):\n",
    "        s=set()\n",
    "        t=0\n",
    "    \n",
    "        for j in range(9):\n",
    "            n=data[i*9+t]['index']\n",
    "            s.add(n)\n",
    "            t+=1\n",
    "            \n",
    "        if(len(s)<9):\n",
    "            print(f\"There is a problem with a row {i}\")\n",
    "        else:\n",
    "            print(f\"Row {i} is fine\")\n",
    "\n",
    "            \n",
    "    print(f\"\\nBoxes:\")        \n",
    "    for i in range(9):\n",
    "        s=set()\n",
    "        t=0\n",
    "        b=(i*3)+(((i*3)//9)*18)\n",
    "        \n",
    "        for j in range(9):\n",
    "            n=data[(b+j)+((j*3)//9)*6]['index']\n",
    "            s.add(n)\n",
    "            \n",
    "        if(len(s)<9):\n",
    "            print(f\"There is a problem with a box {i}\")\n",
    "        else:\n",
    "            print(f\"Box {i} is fine\")\n",
    "            \n",
    "            \n",
    "superCheck()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "worked: 193\n",
      "wrong: 807\n",
      "time: 0.011415155440414508\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import time\n",
    "\n",
    "worked=0\n",
    "wrong=0\n",
    "times=[]\n",
    "\n",
    "for i in range(1000):\n",
    "    try:\n",
    "        start = time.process_time()\n",
    "\n",
    "        data = {}\n",
    "\n",
    "        for i in range(81):\n",
    "            data[i]={'index':i,\n",
    "                     'col':i%9,\n",
    "                     'row':i//9,\n",
    "                     'value':0,\n",
    "                     'box':i//3 - 3*(i//9 - (i//9)//3),\n",
    "                     'pos':[1,2,3,4,5,6,7,8,9],\n",
    "                     'state':'ready'}\n",
    "\n",
    "\n",
    "        def removeOther(r,c,b,n):\n",
    "            for i in range(81):\n",
    "                if (len(data[i]['pos']) > 0) and (n in data[i]['pos']):\n",
    "                    if(data[i]['row']==r) or (data[i]['col']==c) or (data[i]['box']==b):\n",
    "                        data[i]['pos'].remove(n)\n",
    "        #                 print(data[i]['pos'])\n",
    "\n",
    "        def check():\n",
    "        #     print('check')\n",
    "            for i in range(81):\n",
    "                if (len(data[i]['pos']) < 2) and (len(data[i]['pos']) > 0) and (data[i]['state'] == 'ready'):\n",
    "                    data[i]['value']=random.choice(data[i]['pos'])\n",
    "                    data[i]['state']='checked'\n",
    "        #             print(data[i]['index'], data[i]['value'])\n",
    "                    removeOther(data[i]['row'], data[i]['col'], data[i]['box'], data[i]['value'])\n",
    "\n",
    "        for i in range(81):\n",
    "            if data[i]['state'] == 'ready':\n",
    "        #         print(i)\n",
    "                data[i]['value']=random.choice(data[i]['pos'])\n",
    "                data[i]['state']='checked'\n",
    "        #         print(data[i]['index'], data[i]['value'])\n",
    "                removeOther(data[i]['row'], data[i]['col'], data[i]['box'], data[i]['value'])\n",
    "                check()\n",
    "        worked+=1\n",
    "        \n",
    "        end=(time.process_time() - start)\n",
    "        times.append(end)\n",
    "    except:\n",
    "        wrong+=1\n",
    "        \n",
    "print(f\"worked: {worked}\\nwrong: {wrong}\\ntime: {sum(times) / len(times)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "max time: 0.171875\n",
      "min time: 0.0\n",
      "average time: 0.0313125\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import time\n",
    "\n",
    "times=[]\n",
    "\n",
    "for i in range(1000):\n",
    "    start = time.process_time()\n",
    "    \n",
    "    sudoku()\n",
    "        \n",
    "    end=(time.process_time() - start)\n",
    "    times.append(end)\n",
    "        \n",
    "print(f\"max time: {max(times)}\\nmin time: {min(times)}\\naverage time: {sum(times) / len(times)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1: 0.015625 s\n",
      "10: 0.25 s\n",
      "50: 1.59375 s\n",
      "100: 3.109375 s\n",
      "300: 9.234375 s\n",
      "500: 15.03125 s\n",
      "700: 21.78125 s\n",
      "1000: 30.453125 s\n",
      "[0.015625, 0.25, 1.59375, 3.109375, 9.234375, 15.03125, 21.78125, 30.453125]\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "\n",
    "times=[1, 50, 100, 300, 500, 700, 1000]\n",
    "results=[]\n",
    "\n",
    "\n",
    "for i in range(len(times)):\n",
    "    start = time.process_time()\n",
    "    for j in range(times[i]):\n",
    "        sudoku()\n",
    "\n",
    "    results.append(time.process_time() - start)\n",
    "    print(f\"{times[i]}: {results[len(results)-1]} s\")\n",
    "\n",
    "print(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x360 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "\n",
    "f, axs = plt.subplots(1,2, figsize=(10, 5))\n",
    "axs[0].plot(times, results, color='green', marker='o', markersize=5, linestyle='dashed', linewidth=2)\n",
    "axs[0].grid()\n",
    "\n",
    "axs[1].loglog(times, results, color='blue', marker='o', markersize=5, linewidth=2)\n",
    "axs[1].grid()\n",
    "\n",
    "plt.tight_layout()"
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

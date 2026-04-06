# %%
import pandas as pd
from scipy.stats.mstats import gmean, hmean
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

a_mean = my_dataset.Zr.mean()
g_mean = gmean(my_dataset['Zr'])
h_mean = hmean(my_dataset['Zr'])

print ('-------')
print ('arithmetic mean')
print ("{0:.1f} [ppm]".format(a_mean))
print ('-------')

print ('geometric mean')
print ("{0:.1f} [ppm]".format(g_mean))
print ('-------')

print ('harmonic mean')
print ("{0:.1f} [ppm]".format(h_mean))
print ('-------')

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins='auto', density=True, edgecolor='k', label='Measurements Hist', alpha=0.8) 
ax.axvline(a_mean, color='purple', label='Arithmetic mean', linewidth=2)
ax.axvline(g_mean, color='orange',  label='Geometric mean', linewidth=2)
ax.axvline(h_mean, color='green',  label='Harmonic mean', linewidth=2)
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()

'''
Output:
-------
arithmetic mean
365.4 [ppm]
-------
geometric mean
348.6 [ppm]
-------
harmonic mean
333.8 [ppm]
-------
'''

# %%
import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

median = my_dataset.Zr.median()

print ('-------')
print ('median')
print("{0:.1f} [ppm]".format(median))
print ('-------')

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins=20, density=True, edgecolor='k', label="Measurements Hist", alpha=0.8) 
ax.axvline(median, color='orange', label='Median', linewidth=2)
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()

'''
Output:
-------
median
339.4 [ppm]
-------
'''

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

hist, bin_edges = np.histogram(my_dataset['Zr'], bins= 20, density=True)
modal_value = (bin_edges[hist.argmax()] +  bin_edges[hist.argmax()+1])/2

print ('modal value: {0:.0f} [ppm]'.format(modal_value))

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins=20, density=True, edgecolor='k', label="Measurements Hist", alpha=0.8) 
ax.axvline(modal_value, color="orange", label="Modal value", linewidth=2)
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()

'''
Output: modal value: 277 [ppm]
'''


# %%
import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

my_range = my_dataset['Zr'].max()- my_dataset['Zr'].min()

print ('-------')
print ('Range')
print("{0:.0f}".format(my_range))
print ('-------')

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins=20, density=True, edgecolor='k', label='Measurements Hist') 
ax.axvline(my_dataset['Zr'].max(), color='purple', label='Max value', linewidth=2)
ax.axvline(my_dataset['Zr'].min(), color='green', label='Min value', linewidth=2)
ax.axvspan(my_dataset['Zr'].min(), my_dataset['Zr'].max(), alpha=0.1, color='orange', label='Range = ' + "{0:.0f}".format(my_range) + ' ppm')
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()



# %%
import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

variance =  my_dataset['Zr'].var()
stddev =  my_dataset['Zr'].std()

print ('-------')
print ('Variance')
print("{0:.0f} [square ppm]".format(variance))
print ('-------')
print ('Standard Deviation')
print("{0:.0f} [ppm]".format(stddev))
print ('-------')

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins= 20, density = True, edgecolor='k', label='Measurements Hist') 
ax.axvline(my_dataset['Zr'].mean()-stddev, color='purple', label=r'mean - 1$\sigma$', linewidth=2)
ax.axvline(my_dataset['Zr'].mean()+stddev, color='green', label=r'mean + 1$\sigma$', linewidth=2)
ax.axvspan(my_dataset['Zr'].mean()-stddev, my_dataset['Zr'].mean()+stddev, alpha=0.1, color='orange', label=r'mean $\pm$ 1$\sigma$')
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()

'''
Output:
-------
Variance
14021 [square ppm]
-------
Standard Deviation
118 [ppm]
-------
'''

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

q1 = np.percentile(my_dataset.Zr, 25, method = 'midpoint') 
q3 = np.percentile(my_dataset.Zr, 75, method = 'midpoint') 
  
iqr = q3 - q1 # Interquaritle range (IQR)  

print ('-------')
print ('Interquaritle range (IQR): {0:.0f} [ppm]'.format(iqr))
print ('-------')

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins='auto', density=True, edgecolor='k', label='Measurements Hist') 
ax.axvline(q1, color='purple', label='Q1', linewidth=2)
ax.axvline(q3, color='green', label='Q3', linewidth=2)
ax.axvspan(q1, q3, alpha=0.1, color='orange', label='Interquaritle range (IQR)')
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()

'''
Output:
-------
Interquaritle range (IQR): 164 [ppm]
-------
'''

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

a_mean = my_dataset.Zr.mean()

median = my_dataset.Zr.median()

hist, bin_edges = np.histogram(my_dataset['Zr'], bins=20, density=True)
modal_value = (bin_edges[hist.argmax()] +  bin_edges[hist.argmax()+1])/2

fig, ax = plt.subplots()
ax.hist(my_dataset.Zr, bins=20, density=True, edgecolor='k', label="Measurements Hist") 
ax.axvline(modal_value, color='orange', label='Modal Value', linewidth=2)
ax.axvline(median, color='purple',  label='Median Value', linewidth=2)
ax.axvline(a_mean, color='green',  label='Arithmetic mean', linewidth=2)
ax.set_xlabel('Zr [ppm]')
ax.set_ylabel('Probability density')
ax.legend()



# %%
import numpy as np
from scipy.stats import skew

a_mean = my_dataset.Zr.mean()
median = my_dataset.Zr.median()
hist, bin_edges = np.histogram(my_dataset['Zr'], bins=20, density=True)
modal_value = (bin_edges[hist.argmax()] + bin_edges[hist.argmax()+1])/2
standard_deviation = my_dataset['Zr'].std()

a1 = (a_mean - modal_value) / standard_deviation 
a2 = 3 * (a_mean - median) / standard_deviation
g1 = skew(my_dataset['Zr'])

print ('-------')
print ("Pearson's first coefficient of skewness: {:.2f}".format(a1))
print ("Pearson's 2nd moment of skewness: {:.2f}".format(a2))
print ("Fisher-Pearson's coefficient of skewness: {:.2f}".format(g1))
print ('-------')

'''
Output:
-------
Pearson's first coefficient of skewness: 0.74
Pearson's 2nd moment of skewness: 0.66
Fisher-Pearson's coefficient of skewness: 1.26
-------
'''

# %%
import pandas as pd

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

statistics = my_dataset[['Ba','Sr','Zr','La']].describe()

print(statistics)

'''
Output:
                Ba           Sr          Zr          La
count   370.000000   369.000000  370.000000  370.000000
mean    789.733259   516.422115  365.377397   74.861088
std     523.974960   241.922439  118.409962   18.256772
min       0.000000     9.541958  185.416567   45.323289
25%     297.402777   319.667551  274.660242   61.745228
50%     768.562055   490.111131  339.412064   71.642167
75%    1278.422645   728.726116  438.847368   83.670805
max    2028.221963  1056.132069  920.174406  169.550008
'''   

# %%
import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

fig, ax = plt.subplots()
my_flierprops = dict(markerfacecolor='#f8e9a1', markeredgecolor='#24305e', marker='o')
my_medianprops = dict(color='#f76c6c', linewidth = 2)
my_boxprops = dict(facecolor='#a8d0e6', edgecolor='#24305e')
ax.boxplot(my_dataset.Zr, patch_artist = True, notch=True, flierprops=my_flierprops, medianprops=my_medianprops, boxprops=my_boxprops) 
ax.set_ylabel('Zr [ppm]')
ax.set_xticks([1])
ax.set_xticklabels(['all Epochs'])
plt.show()

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

fig, ax = plt.subplots()
ax = sns.boxplot(x="Epoch", y="Zr", data=my_dataset,  palette="Set3")




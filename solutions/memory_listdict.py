import sys
sizes_dict = []
sizes_list = []
for n_elements in range(100):
    a = {i:str(i) for i in range(n_elements)}
    sizes_dict.append(sys.getsizeof(a))

    b = list(range(n_elements))
    sizes_list.append(sys.getsizeof(b))

import matplotlib.pyplot as plt
plt.plot(sizes_dict, label='dict')
plt.plot(sizes_list, label='list')
plt.legend();

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speedtest

def get_internet_speed():
    st = speedtest.Speedtest()
    
    download_speed = st.download() / 1_000_000  # in megabits per second
    upload_speed = st.upload() / 1_000_000  # in megabits per second
    
    return download_speed, upload_speed

if __name__ == "__main__":
    try:
        download_speed, upload_speed = get_internet_speed()
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
    except Exception as e:
        print(f"An error occurred: {e}")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install opencv-python


# In[4]:


import cv2


# In[5]:


image=cv2.imread('chetnagupta.jfif')


# In[6]:


gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# In[7]:


invert=cv2.bitwise_not(gray_img)


# In[8]:


blur=cv2.GaussianBlur(invert,(21,21),0)


# In[9]:


inverted_blur=cv2.bitwise_not(blur)


# In[10]:


sketch=cv2.divide(gray_img,inverted_blur,scale=256.0)


# In[11]:


cv2.imwrite('sketch.png',sketch)


# In[ ]:





# How the Sobel Operator Works

install 4 libraries by pip(cv2, numpy, scipy, matplotlib) in own venv 

```
pip install numpy, scipy, matplotlib, opencv-python
```

then run the code with other value on Sobel Edge Detector 


```python
F1 = np.array([[-1, 0, 0],
               [0, 0, 0],
               [0, 0, +1]])
```
like these

```python
F2 = np.array([[0, -1, 0],
               [-1, +4, -1],
               [0, -1, 0]])
```

```python
F3 = np.array([[-0.5, -1, -0.5],
               [-1, +6, -1],
               [-0.5, -1, -0.5]])
```

and whatching how this work.

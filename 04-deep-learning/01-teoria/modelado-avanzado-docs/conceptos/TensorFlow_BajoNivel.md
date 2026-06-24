## Custom Models and Training with TensorFlow.

Up until now, we’ve used only TensorFlow’s high-level API, Keras, but it
already got us pretty far: we built various neural network architectures,
including regression and classification nets, Wide & Deep nets, and self-
normalizing nets, using all sorts of techniques, such as batch normalization,
dropout, and learning rate schedules. In fact, 95% of the use cases you will
encounter will not require anything other than Keras (and tf.data; see
Chapter 13). But now it’s time to dive deeper into TensorFlow and take a
look at its lower-level Python API. This will be useful when you need extra
control to write custom loss functions, custom metrics, layers, models,
initializers, regularizers, weight constraints, and more. You may even need to
fully control the training loop itself; for example, to apply special
transformations or constraints to the gradients (beyond just clipping them) or
to use multiple optimizers for different parts of the network. We will cover all
these cases in this chapter, and we will also look at how you can boost your
custom models and training algorithms using TensorFlow’s automatic graph
generation feature. But first, let’s take a quick tour of TensorFlow.

### A Quick Tour of TensorFlow
As you know, TensorFlow is a powerful library for numerical computation,
particularly well suited and fine-tuned for large-scale machine learning (but
you can use it for anything else that requires heavy computations). It was
developed by the Google Brain team and it powers many of Google’s large-
scale services, such as Google Cloud Speech, Google Photos, and Google
Search. It was open sourced in November 2015, and it is now the most
widely used deep learning library in the industry:1 countless projects use
TensorFlow for all sorts of machine learning tasks, such as image
classification, natural language processing, recommender systems, and time
series forecasting.

So what does TensorFlow offer? Here’s a summary:
Its core is very similar to NumPy, but with GPU support.
It supports distributed computing (across multiple devices and servers).
It includes a kind of just-in-time (JIT) compiler that allows it to optimize
computations for speed and memory usage. It works by extracting the
computation graph from a Python function, optimizing it (e.g., by
pruning unused nodes), and running it efficiently (e.g., by automatically
running independent operations in parallel).
Computation graphs can be exported to a portable format, so you can
train a TensorFlow model in one environment (e.g., using Python on
Linux) and run it in another (e.g., using Java on an Android device).
It implements reverse-mode autodiff (see Chapter 10 and Appendix B)
and provides some excellent optimizers, such as RMSProp and Nadam
(see Chapter 11), so you can easily minimize all sorts of loss functions.
TensorFlow offers many more features built on top of these core features: the
most important is of course Keras,⁠ 2 but it also has data loading and
preprocessing ops (tf.data, tf.io, etc.), image processing ops (tf.image), signalprocessing ops (tf.signal), and more (see Figure 12-1 for an overview of
TensorFlow’s Python API).

### Using TensorFlow like NumPy.
TensorFlow’s API revolves around tensors, hence the name Tensor-Flow. A tensor is
usually a multidimensional array (exactly like a NumPy ndarray), but it can also hold
a scalar (a simple value, such as 42). These tensors will be important when we create
custom cost functions, custom metrics, custom layers and more, so let’s see how to
create and manipulate them.
Tensors and Operations
You can easily create a tensor, using tf.constant(). For example, here is a tensor
representing a matrix with two rows and three columns of floats:

### Tensors and NumPy
Tensors play nice with NumPy: you can create a tensor from a NumPy array, and vice
versa, and you can even apply TensorFlow operations to NumPy arrays and NumPy
operations to tensors:

### Type Conversions
Type conversions can significantly hurt performance, and they can easily go unno‐
ticed when they are done automatically. To avoid this, TensorFlow does not perform
any type conversions automatically: it just raises an exception if you try to execute an operation on tensors with incompatible types. For example, you cannot add a float
tensor and an integer tensor, and you cannot even add a 32-bit float and a 64-bit float:


### Variables
The tf.Tensor values we’ve seen so far are immutable: we cannot modify
them. This means that we cannot use regular tensors to implement weights in
a neural network, since they need to be tweaked by backpropagation. Plus,
other parameters may also need to change over time (e.g., a momentum
optimizer keeps track of past gradients). What we need is a tf.Variable:


### Other Data Structures
TensorFlow supports several other data structures, including the following
(see the “Other Data Structures” section in this chapter’s notebook or
Appendix C for more details):


- Sparse tensonrs
- Tensor arrays
- Ragged Tensors
- String tensors
- Sets
- Queues

### Customizing Models and Training Algorithms
You’ll start by creating a custom loss function, which is a straightforward and
common use case.

#### Custom Loss Functions

#### Saving and Loadin Models Taht Contain Custom Components

#### Custom Activation Functions, Initializers, Regularizers, and
Constraints

#### Custom Metrics

#### Custom Models

#### Custom Layers

#### Losses and Metrics Based on Model Internals

#### Computing Gradients Using Autodiff

#### Custom Training Loops

### TensorFlow Functions and Graphs
Back in TensorFlow 1, graphs were unavoidable (as were the complexities
that came with them) because they were a central part of TensorFlow’s API.
Since TensorFlow 2 (released in 2019), graphs are still there, but not as
central, and they’re much (much!) simpler to use. To show just how simple,
let’s start with a trivial function that computes the cube of its input:

``` python
def cube(x):
  return x ** 3
```

#### AutoGraph and Tracing
So how does TensorFlow generate graphs? It starts by analyzing the Python
function’s source code to capture all the control flow statements, such as for
loops, while loops, and if statements, as well as break, continue, and return
statements.


#### TF Function Rules
Most of the time, converting a Python function that performs TensorFlow
operations into a TF function is trivial: decorate it with @tf.function or let
Keras take care of it for you. However, there are a few rules to respect:

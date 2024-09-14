Greetings of the day, I am Bernis Mariya X. I would like to attach my solutions as python codes for all the four problem statements.

QUESTION 1 : Are Django signals executed synchronously or asynchronously?

Solution : The output clearly shows that the signal handler is triggered and completes its execution before the main process prints "User created." This confirms that Django signals are executed synchronously by default, meaning the main process waits for the signal handler to finish before continuing. 
If Django signals were asynchronous, "User created" would be printed immediately after saving the user, without waiting for the signal handler to finish.
Since the signal handler runs completely before the final message, it proves synchronous behavior.

QUESTION 2 : Whether Django signals run in the same thread as the caller?

Solution : The output shows that both the main function and the signal receiver are running in the same thread, which conclusively proves that Django signals are executed in the same thread as the caller by default. If signals were executed in a different thread, the output for the signal receiver’s thread would be different from the main thread. hence both parts of the code execute in the same thread. 

QUESTION 3 : Whether Django signals run in the same database transaction as the caller?

Solution : The signal handler successfully accesses the uncommitted user , proving that Django signals run within the same database transaction as the caller.
If the signal ran in a different transaction, the uncommitted user would not be visible, and the signal handler would print "Signal receiver cannot access the user." Therefore, this demonstrates that by default, Django signals are executed within the same database transaction as the caller.

QUESTION 4 : Implement a Rectangle class.

Solution : The Rectangle class is designed to take length and width as inputs and allows iteration over its instances, returning each dimension in the form of dictionaries (e.g., {'length': <value>}, {'width': <value>}).

For every Problem statement there is a code snippet attached with the python code.

Thankyou.

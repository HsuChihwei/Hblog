
Category: python
Tags: code,threading
Author: zhiwei.xu
Date: 2019-08-06 11:47:34
Modified: 2019-08-06 16:22:02

# threadPool

```python
import threading
import traceback

from abc import ABCMeta, abstractmethod
# from multiprocessing.dummy import Pool  # 多线程模式
from multiprocessing.pool import Pool  # 多进程模式


class Executor(metaclass=ABCMeta):
    """公共执行器
    """
    def __init__(self, process_num):
        """init the executor

        Arguments:
            process_num {int} -- the numbers of worker pool
        """
        self.pool = Pool(process_num)
        self._result = []

    @abstractmethod
    def _store(self, item):
        """callback function of worker, add return to result

        Arguments:
            item {tuple} -- one result of tasks
        """
        pass

    def worker(self, tasks):
        """add task into worker pool

        Arguments:
            tasks {list} -- a list of tasks
        """
        try:
            for func, items in tasks:
                self.pool.apply_async(func, args=(items,), callback=self._store)
        except:
            print(traceback.format_exc())

    def wait(self):
        """close the pool
        """
        self.pool.close()
        self.pool.join()

    def result(self):
        """return the result of tasks

        Returns:
            list -- all result of tasks
        """
        return self._result


class TelExecutor(Executor):
    """ a subclass of Executor use for tel find name"""

    def _store(self, item):
        """store the result of tasks

        Arguments:
            item {tuple} -- one result of tasks
        """
        if item:
            self._result.append(item)

        # 提前结束条件
        if item[0] == 'es' and item[3] is True:
            self.pool.terminate()


class NameExecutor(Executor):
    """ a subclass of Executor use for name find tel"""

    def _store(self, item):
        """store the result of tasks

        Arguments:
            item {tuple} -- one result of tasks
        """
        if item:
            self._result.append(item)


def multi_result(tel_tasks, name_tasks):
    """multi deal with tel tasks and name tasks, return result

    Arguments:
        tel_tasks {list} -- the tasks of tel find name
        name_tasks {list} -- the tasks of name find tel

    Returns:
        list -- the result of tasks
    """
    tel_exec = TelExecutor(len(tel_tasks))  # 号查名执行器
    name_exec = NameExecutor(len(name_tasks))  # 名查号执行器
    try:
        # 开启多线程，同时启动任务
        t1 = threading.Thread(target=tel_exec.worker, args=(tel_tasks,))
        t2 = threading.Thread(target=name_exec.worker, args=(name_tasks,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        # 关闭执行器，释放资源
        tel_exec.wait()
        name_exec.wait()

        return [tel_exec.result(), name_exec.result()]
    except:
        print(traceback.format_exc())
        return [(), ()]


if __name__ == '__main__':
    import random
    import time

    def test(item):
        """test function

        Arguments:
            item {tuple} -- a tuple of args for test task

        Returns:
            tuple -- the result of test task
        """
        try:
            sleeps = 1 + random.random()
            time.sleep(sleeps)
        except:
            print(traceback.format_exc())
        return item

    tel_tasks = name_tasks = [(test, ('es', 'data', 'sid', True)),
                                (test, ('tyc', 'data', 'sid', True)),
                                (test, ('map', 'data', 'sid', True))]

    ret = multi_result(tel_tasks, name_tasks)
    print('tel:', ret[0])
    print('name:', ret[1])
```

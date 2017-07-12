import numpy as np
import matplotlib.pyplot as plt
plt.ion()
# primo
from datasets import h_shaped_dataset, two_moon_dataset, gaussians_dataset
from utils import plot_boundary, cmap, plot_2d_dataset


class AdaBoostClassifier:
    """
    Function that models a Adaboost classifier
    """

    def __init__(self, n_learners):
        """
        Model constructor

        Parameters
        ----------
        n_learners: int
            number of weak classifiers.
        """

        # initialize a few stuff
        self.n_learners = n_learners
        self.alphas = np.zeros(shape=n_learners)
        self.dims = np.zeros(shape=n_learners, dtype=np.int32)
        self.splits = np.zeros(shape=n_learners)
        self.verses = np.zeros(shape=n_learners, dtype=np.int32)

        self.possible_labels = None

    def fit(self, X, Y, verbose=False):
        """
        Trains the model.

        Parameters
        ----------
        X: ndarray
            features having shape (n_samples, dim).
        Y: ndarray
            class labels having shape (n_samples,).
        verbose: bool
            whether or not to visualize the learning process.
            Default is False
        """

        # some inits
        n, d = X.shape
        if d != 2:
            verbose = False  # only plot learning if 2 dimensional

        self.possible_labels = np.unique(Y)

        # only binary problems please
        assert self.possible_labels.size == 2, 'Error: data is not binary'

        # initialize the sample weights as equally probable

        # start training
        for l in xrange(0, self.n_learners):

            # choose the indexes of 'difficult' samples (np.random.choice)

            # extract 'difficult' samples

            # search for a weak classifier
            error = 1
            while error > 0.5:

                # select random feature (np.random.choice)

                # select random split (np.random.uniform)

                # select random verse (np.random.choice)

                # compute assignment

                # compute error

            # save weak learner parameter

            # update sample weights

            if verbose:
                # plot
                plt.clf()
                plt.scatter(cur_X[:, 0], cur_X[:, 1], c=cur_labels, s=sample_weights[sample_indexes]*50000,
                            cmap=cmap, edgecolors='k')
                M1, m1 = np.max(X[:, 1]), np.min(X[:, 1])
                M0, m0 = np.max(X[:, 0]), np.min(X[:, 0])
                if cur_dim == 0:
                    plt.plot([cur_split, cur_split], [m1, M1], 'k-', lw=5)
                else:
                    plt.plot([m0, M0], [cur_split, cur_split], 'k-', lw=5)
                plt.xlim([m0, M0])
                plt.ylim([m1, M1])
                plt.xticks([])
                plt.yticks([])
                plt.title('Iteration: {:04d}'.format(l))
                plt.savefig('tex/img/boosting/gif/{:03d}.pdf'.format(l), bbox_inches='tight')
                plt.waitforbuttonpress(timeout=0.1)

    def predict(self, X):
        """
        Function to perform predictions over a set of samples.
        
        Parameters
        ----------
        X: ndarray
            examples to predict. shape: (n_examples, d).

        Returns
        -------
        ndarray
            labels for each examples. shape: (n_examples,).

        """
        n, d = X.shape

        pred_all_learners = np.zeros(shape=(n, self.n_learners))

        for l, cur_dim, cur_split, cur_verse in zip(range(0, self.n_learners), self.dims, self.splits, self.verses):
            # compute assignment
            pass

        # weight for learners efficiency


        # compute predictions
        

        return pred


def main_adaboost():
    """
    Main function for testing Adaboost.
    """

    X_train, Y_train, X_test, Y_test = h_shaped_dataset()
    # X_train, Y_train, X_test, Y_test = gaussians_dataset(2, [100, 150], [[1, 3], [-4, 8]], [[2, 3], [4, 1]])
    # X_train, Y_train, X_test, Y_test = two_moon_dataset(n_samples=300, noise=0.2)

    # visualize dataset
    plot_2d_dataset(X_train, Y_train, 'Training')

    # train model and predict
    model = AdaBoostClassifier(n_learners=100)
    model.fit(X_train, Y_train, verbose=True)
    P = model.predict(X_test)

    # visualize the boundary!
    plot_boundary(X_train, Y_train, model)

    # evaluate and print error
    error = float(np.sum(P != Y_test)) / Y_test.size
    print error

# entry point
if __name__ == '__main__':
    main_adaboost()

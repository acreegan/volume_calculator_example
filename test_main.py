from main import calculate_volume
import numpy as np
import numpy.testing
import matplotlib.pyplot as plt


def test_calculate_volume():
    sample_frequency = 100
    duration = np.pi
    time = np.linspace(0, np.pi, int(duration*sample_frequency))
    flow = np.sin(time)
    #
    # plt.plot(time, flow)
    # plt.show()

    correct_max_volume = 2

    volume = calculate_volume(flow, 1/sample_frequency, initial=0)
    max_volume = volume[np.argmax(volume)]

    np.testing.assert_almost_equal(correct_max_volume, max_volume, decimal=2)

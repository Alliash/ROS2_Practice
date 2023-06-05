# ROS2_Practice

# Checkpoint

SSD_CheckPoint_Adam_fine_500
https://drive.google.com/file/d/1n6i2UMBwnhj-ze7vY8vZAvRltjW7NqeN/view?usp=sharing

SSD_CheckPoint_SGD_drone_200_0.1
https://drive.google.com/file/d/16UGJirr4cOyysztQz-AlRlpTqxc_2oO6/view?usp=sharing

SSD_CheckPoint_SGD_fine_200
https://drive.google.com/file/d/1_Hl9VVuXICg7qOM6zOylZRWyge6TZx0E/view?usp=sharing

SSD_CheckPoint_SGD_fine_500
https://drive.google.com/file/d/1iuLCzKIcyVX69ViPu3-E7vV4bBwVQn-l/view?usp=sharing

# custom_test_video
https://drive.google.com/file/d/1vd_VjFPXacO7ei-0VZeiRxaiybJmwWmO/view?usp=sharing
'\n'
https://drive.google.com/file/d/1fShOH7GZPoLSlGpTXjN84470WdkTIGZY/view?usp=sharing


# 영상 Publisher Entry_point 수정(setup.py의 entry point 부분)
```
entry_points={
        'console_scripts': [
        'detection_example = ssd_detection.ssd_detection:main',
        'video_publisher = ssd_detection.video_publisher:main',
        ],
```

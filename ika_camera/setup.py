from setuptools import find_packages, setup

package_name = 'ika_camera'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='asak',
    maintainer_email='abdoorahmansk2004@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'centering_controller = ika_camera.centering_controller:main',
            'dummy_pclaud_listener = ika_camera.dummy_pclaud_listener:main',
            'cmd_pub = ika_camera.cmd_pub:main',
        ],
    },
)

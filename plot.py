import matplotlib.pyplot as plt
unit = ['.M', '.gAPI', '.ohm.m', '.ohm.m', '.pu', '.in', '.in', '.g/cm3', '.us/ft', '.us/ft']
unit_log = ['.M', '.gAPI', '.ln', '.ln', '.pu', '.in', '.in', '.g/cm3', '.us/ft', '.us/ft']
unit_train = ['.M', '.gAPI', '.ln', '.pu', '.us/ft', '.us/ft']
unit_features = ['.M', '.gAPI', '.ln', '.pu', '.us/ft']

def plot_log(df):
    fig, ax = plt.subplots(nrows=1, ncols=len(df.columns)-1, figsize=(20,10), sharey=True)
    colors = ['blue', 'green', 'red', '#008987', 'magenta', 'orange', 'black', 'blue', '#007698', '#EA92B0']

    for i in range(1, len(df.columns)):
        ax[i-1].plot(df[df.columns[i]], df['DEPT'], color=colors[i])
        
        ax[i-1].set_title(df.columns[i])
        ax[i-1].grid(linestyle='--')
        ax[i-1].grid(which='minor', linestyle=':', color='green')
        ax[i-1].minorticks_on()
        ax[i-1].set_ylim(max(df['DEPT']), min(df['DEPT']))
        ax[0].set_ylabel('Depth (m)')
        ax[i-1].set_xlabel(unit[i])
    plt.tight_layout()
    plt.show()
    
def plot_log_res(df):
    fig, ax = plt.subplots(nrows=1, ncols=len(df.columns)-1, figsize=(20,10), sharey=True)
    colors = ['blue', 'green', 'red', '#008987', 'magenta', 'orange', 'black', 'blue', '#007698', '#EA92B0']

    for i in range(1, len(df.columns)):
        ax[i-1].plot(df[df.columns[i]], df['DEPT'], color=colors[i])
        
        ax[i-1].set_title(df.columns[i])
        ax[i-1].grid(linestyle='--')
        ax[i-1].grid(which='minor', linestyle=':', color='green')
        ax[i-1].minorticks_on()
        ax[i-1].set_ylim(max(df['DEPT']), min(df['DEPT']))
        ax[0].set_ylabel('Depth (m)')
        ax[i-1].set_xlabel(unit_log[i])
    plt.tight_layout()
    plt.show()
    
def plot_features(df):
    fig, ax = plt.subplots(nrows=1, ncols=len(df.columns)-1, figsize=(20,10), sharey=True)
    colors = ['blue', 'green', 'red', '#008987', 'magenta', 'orange', 'black', 'blue', '#007698', '#EA92B0']

    for i in range(1, len(df.columns)):
        ax[i-1].plot(df[df.columns[i]], df['DEPT'], color=colors[i])
        
        ax[i-1].set_title(df.columns[i])
        ax[i-1].grid(linestyle='--')
        ax[i-1].grid(which='minor', linestyle=':', color='green')
        ax[i-1].minorticks_on()
        ax[i-1].set_ylim(max(df['DEPT']), min(df['DEPT']))
        ax[0].set_ylabel('Depth (m)')
        ax[i-1].set_xlabel(unit_features[i])
    plt.tight_layout()
    plt.show()
    
def plot_train(df):
    fig, ax = plt.subplots(nrows=1, ncols=len(df.columns)-1, figsize=(20,10), sharey=True)
    colors = ['blue', 'green', 'red', '#008987', 'magenta', 'orange', 'black', 'blue', '#007698', '#EA92B0']

    for i in range(1, len(df.columns)):
        ax[i-1].plot(df[df.columns[i]], df['DEPT'], color=colors[i])
        
        ax[i-1].set_title(df.columns[i])
        ax[i-1].grid(linestyle='--')
        ax[i-1].grid(which='minor', linestyle=':', color='green')
        ax[i-1].minorticks_on()
        ax[i-1].set_ylim(max(df['DEPT']), min(df['DEPT']))
        ax[0].set_ylabel('Depth (m)')
        ax[i-1].set_xlabel(unit_train[i])
    plt.tight_layout()
    plt.show()

# alias
plot_test = plot_train
import matplotlib.pyplot as plt

wl_stat         = [[0,0]]
count_stat      = [[0,0]]
bet_stat        = [[0,0]]
bal_stat        = [[0,1000]]
cardsdrawn_stat = 0

def increase_drawncount(n):
    global cardsdrawn_stat
    cardsdrawn_stat = cardsdrawn_stat + n

def save_winlose(wl):
    global wl_stat
    global cardsdrawn_stat

    last_wl = wl_stat[-1][1]
    wl_stat.append([cardsdrawn_stat,last_wl+wl])

def save_count(count):
    global count_stat
    global cardsdrawn_stat
    count_stat.append([cardsdrawn_stat,count])

def save_bal(bs):
    global cardsdrawn_stat
    global bal_stat
    bal_stat.append([cardsdrawn_stat,bs])

def save_bet(b):
    global cardsdrawn_stat
    global bet_stat
    bet_stat.append([cardsdrawn_stat,b])

def deck_lines(ax,carddata,datadata):
    linetop = max(datadata)
    print linetop
    linebot = min(datadata)

    ncardsplayed =max(carddata)
    
    for n in range(0,10000):
        x=[]
        y=[]

        if n*52>ncardsplayed:
            break
        else:
            for i in [linebot,linetop]:
                x.append(52*n)
                y.append(i)
                ax.plot(x,y,alpha=0.5)
                
def plot_stats(name):

    title = name+': Session playing Stats'
    fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(nrows=3, ncols=2,figsize=(10,6),num=title)
    fig.suptitle(title)

    global count_stat
    x = []
    y = []
    for n in range (0,len(count_stat)):
        x.append(count_stat[n][0])
        y.append(count_stat[n][1])

  #  fig.subplot(221)
    ax1.set_ylabel('Count')
    ax1.set_xlabel('Number of cards')
    ax1.plot(x, y)
    deck_lines(ax1,x,y)
    #ax1.legend()
  #  ax1.grid()

    global wl_stat
    x1=[]
    y1=[]
    for n in range(0,len(wl_stat)):
        x1.append(wl_stat[n][0])
        y1.append(wl_stat[n][1])

  #  fig.subplot(222)
    ax2.set_xlabel('Number of cards')
    ax2.set_ylabel('Win/Lose')
    ax2.plot(x1, y1)
    deck_lines(ax2,x1,y1)
    #ax2.legend()
   # ax2.grid()

    global bet_stat
    x2=[]
    y2=[]
    for n in range(0,len(bet_stat)):
        x2.append(bet_stat[n][0])
        y2.append(bet_stat[n][1])

   # fig.subplot(223)h
    ax3.set_xlabel('Number of cards')
    ax3.set_ylabel('Bet [$]')
    ax3.plot(x2, y2)
    deck_lines(ax3,x2,y2)
    #ax3.legend()
   # ax3.grid()

    global bal_stat
    x3=[]
    y3=[]

    for n in range(0,len(bal_stat)):
        x3.append(bal_stat[n][0])
        y3.append(bal_stat[n][1])

   # fig.subplot(224)
    ax4.set_xlabel('Number of cards')
    ax4.set_ylabel('Balance [$]')
    deck_lines(ax4,x3,y3)
    ax4.plot(x3, y3)
    #ax4.legend()
   # ax4.grid()

    ax5.set_xlabel('Number of cards')
    ax5.set_ylabel('Hand Value')
    ax5.grid()

    ax6.set_xlabel('Number of cards')
    ax6.set_ylabel('something')
    ax6.grid()


    print '\n'+'-'*15
    print 'STATS'
    print 'drawn '+str(cardsdrawn_stat)
    print 'count '+str(count_stat[-1][1])
    print 'wl '+str(wl_stat[-1][1])
    print 'balance'+str(bal_stat[-1][1])
    print 'max bet'+str(max(bet_stat))
    print '-'*15

    fig.tight_layout(rect=[0.0,0.0,1.0,0.95])
    plt.show()
    plt.savefig('Images/'+name+'_stats.pdf')
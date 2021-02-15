'''
    .Description:

    This python script will open UI in which User can enter 
    name of any window service to not only see it's status 
    but user can also modify existence status.
    For Example : If service is Running User can Stop the service,Restart the serivce or viceversa.


    .INPUT:

     There is no command line in
'''


























#####---------------Importing Packages-------------------------#####


from PyQt5 import QtCore, QtGui, QtWidgets # Modeule for GUI
import win32serviceutil # Module to Start,Restart and Stop Service
import psutil # Module to Check Status Of Service,whether it is exist or not.
from PyQt5.QtGui import QIcon
from Logs import Log
#-------------------------------------------------------------------#



######------------Class For UI----------------------------------#####

class Ui_Form_Local(object):
    def __init__(self,obc):
        self.obc = obc
    '''
    Main UI Code for Button,label,
    Text Field. It contain styleshhets and Onclicked Function Defination.

    '''



    def setupUi(self, Form):
        '''
        Setting UI Geometry and StyleSheets

        '''

        ##-------Initializing Main UI Geometry and Back Ground Color----------------#

        Form.setObjectName("Form")
        Form.resize(470, 220)
        Form.setAcceptDrops(True)
        Form.setWindowOpacity(0.9)
        Form.setStyleSheet("background-color: rgb(0,0,0)")

        #----------------------------------------------------------------------------#





        #----------Initializing Font type and Size----------------------------------#

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)

        #----------------------------------------------------------------------------#




        #---------Initailizing Layout------------------------------------------------#

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        #-----------------------------------------------------------------------------#






        # ------Initailizing Label (Enter Service Name) and LineEdit for User Input----#

        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.CheckStatus) #Calling Function Name CheckStatus Every time User type.
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        ##----------------------------------------------------------------------- ---------------------#





        

        #-----Initailizing Label for Service Status------------------------------------------#

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        #-------------------------------------------------------------------------------------#

       





        
        #----------Initializing PushButton for Start, Restart and Stop Service----------------------------# 

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_start = QtWidgets.QPushButton(Form)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.pushButton_start.setFont(font)

        self.pushButton_stop = QtWidgets.QPushButton(Form)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout.addWidget(self.pushButton_stop)
        self.pushButton_stop.setFont(font)

        self.pushButton_restart = QtWidgets.QPushButton(Form)
        self.pushButton_restart.setObjectName("pushButton_restart")
        self.horizontalLayout.addWidget(self.pushButton_restart)
        self.pushButton_restart.setFont(font)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        #--------------------------------------------------------------------------------------------------#
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Team 2: Local Machine"))
        Form.setWindowIcon(QIcon('team2.png'))

        ##--------------Label Style Sheet and Name-----------------------------------------##
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color: #ffffff\">Enter Service Name : </span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color: #ffffff\">Status of Service : </span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color: #ffffff\">Status</span></p></body></html>"))
        #------------------------------------------------------------------------------------------------------------------------------------------------------#


        #-------------------Start Button Functianilty---------------------------#
        self.pushButton_start.setText(_translate("Form", "Start"))
        self.pushButton_start.setEnabled(False) #start Button is Disabled
        self.pushButton_start.clicked.connect(self.Start)
        #-----------------------------------------------------------------------#


        #--------------------Stop Button Functionality--------------------------#
        self.pushButton_stop.setText(_translate("Form", "Stop"))
        self.pushButton_stop.setEnabled(False) # stop Button is Disabled
        self.pushButton_stop.clicked.connect(self.Stop)
        #-------------------------------------------------------------------------#


        #--------------------Restart Button Functionality -------------------------#
        self.pushButton_restart.setText(_translate("Form", "Restart"))
        self.pushButton_restart.setEnabled(False) # Restart Button is Disabled
        self.pushButton_restart.clicked.connect(self.Restart)

        #---------------------------------------------------------------------------#



        #----------------------LineEdit and Buttons StyleSheets------------------------------#
        self.lineEdit.setStyleSheet("color:#0000CC")

        self.pushButton_start.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color :#9933FF;"
                             "}"
                             "{"
                             "font-size :40px;"
                             "}"
                             )
        self.pushButton_stop.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color :#9933FF;"
                             "}"
                             "{"
                             "font-size :40px;"
                             "}"
                             ) 
        self.pushButton_restart.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightblue;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color :#9933FF;"
                             "}"
                             "{"
                             "font-size :40px;"
                             "}"
                             )
        #------------------------------------------------------------------------------------------------------------#


    def Restart(self):
        loc=Log('User RESTARTED Service --- {}'.format(self.lineEdit.text()))
        '''
        This Function will get Triggered When User will press Restart Button

        '''
        _translate = QtCore.QCoreApplication.translate
        self.service_name = self.lineEdit.text()
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;color:#ffffff\">Service Restarted</span></p></body></html>"))
        

        #------------------Restarting Service---------------------------------#
        win32serviceutil.RestartService(self.service_name)
        #----------------------------------------------------------------------



        #-----Enabling and Disabling PushButtons-------------------
        self.pushButton_stop.setEnabled(True)
        self.pushButton_start.setEnabled(False)
        self.pushButton_restart.setEnabled(True)
        #-----------------------------------------------------------#



    def Start(self):
        loc=Log('User STARTED Service --- {}'.format(self.lineEdit.text()))
        '''
        This Function will get Trigereed When User will Press Start Button

        '''
        _translate = QtCore.QCoreApplication.translate
        self.service_name = self.lineEdit.text()
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;color:#ffffff\">Service Exist and Service Started</span></p></body></html>"))

        #-------------Starting Service-------------------
        win32serviceutil.StartService(self.service_name)
        #--------------------------------------------------

        #-----------Enabling and Disabling Push Buttons-----------------------
        self.pushButton_stop.setEnabled(True)
        self.pushButton_start.setEnabled(False)
        self.pushButton_restart.setEnabled(True)
        #---------------------------------------------------------------------
        
    def Stop(self):
        loc=Log('User STOPPED Service --- {}'.format(self.lineEdit.text()))
        '''
        This Function will get Triggered when user will press Stop Button

        '''
        _translate = QtCore.QCoreApplication.translate
        self.service_name = self.lineEdit.text()
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;color:#ffffff\">Service Exist and Service is Stopped</span></p></body></html>"))

        #------------Stopping Service------------#
        win32serviceutil.StopService(self.service_name)

        #---------------------------------------------

        #----------Enabling and Disabling PushButtons------------------------
        self.pushButton_stop.setEnabled(False)
        self.pushButton_start.setEnabled(True)
        self.pushButton_restart.setEnabled(True)
        #---------------------------------------------------------------------
        



    def CheckStatus(self):

        '''
        This Function will run continously whenever user will type or change text 

        '''
        _translate = QtCore.QCoreApplication.translate
        self.user_input=self.lineEdit.text() # Name of Service Entered By User
    


        def getService(name):

            '''
            This function will take service name as input
            Function to check whether window service exist or not
            If Service do no exist it will return None as output.

            '''

            service = None
            try:
                service = psutil.win_service_get(name)
                service = service.as_dict()
            except Exception as ex:
                print(str(ex))
            return service

        service = getService(self.user_input) 
        

        if service and service['status'] == 'running':
            #Checking IF service Exist and it is Running
            loc=Log('User CHECKED Status of  Service --- {}'.format(self.lineEdit.text()))
            
            
            self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;color:#ffffff\">Service Exist and Service is Running</span></p></body></html>"))

            #------------Enabling and Disabling PushButtons-----------------------
            self.pushButton_stop.setEnabled(True)
            self.pushButton_restart.setEnabled(True)
            #---------------------------------------------------------------------

           

        elif service and service['status'] !='running':
            # Checking IF service Exist and IT is not Running
            loc=Log('User CHECKED Status of  Service ---- {}'.format(self.lineEdit.text()))
            self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;color:#ffffff\">Service Exist and Service is Not Running</span></p></body></html>"))
            self.pushButton_start.setEnabled(True) # --------------Enabling and Disabling PushButton
            

        else:
            # IF service Do not Exist 
            self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;color:#ffffff\">Service Do Not Exist</span></p></body></html>"))
            loc=Log('User CHECKED Status of  Service --- {}'.format(self.lineEdit.text()))
            #----------------------Enabling and Disabling PushButtons----------------------------
            self.pushButton_start.setEnabled(False)
            self.pushButton_stop.setEnabled(False)
            self.pushButton_restart.setEnabled(False)
            #--------------------------------------------------------------------------------------


        
           
'''

if __name__ == "__main__":
    import ctypes, sys

    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        # Code of your program here
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form2 = QtWidgets.QWidget()
        ui2 = Ui_Form()
        ui2.setupUi(Form2)
        Form2.show()
        sys.exit(app.exec_())
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
'''
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Dialogs 
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    id: "workSpaceDirectory" // root of all
    width: Screen.width
    height: Screen.height
    title: "3D Scanner"
    
    Rectangle {
        id: "addWorkspaceFrame"
        radius: 20
        width: parent.width/2
        height: parent.height/2
        anchors.centerIn: parent 
        
        
            
             Rectangle {
                id:"workspaceDirectoryRectangle"
                x:24
                y:24
            Text {
                            id: "workspaceDirectorylabel"
                            text: "Workspace Directory"
                            height: contentItem.implicitHeight
                            font.pixelSize: 25
                            font.bold: true
                            font.weight: 600
                            font.family: "Segoe UI Variable"
                        }
                    }
                    
                    Rectangle {
                        x:24
                       //width:contentItem.implicitWidth
                      
                        id: "textFieldRectangle"
                        anchors.top:workspaceDirectoryRectangle.bottom
                        anchors.topMargin:100
                        
                        FileDialog {
                            id: fileDialog
                            title: "Select a File"
                            nameFilters: ["All Files (*)"]
                            visible: false
                            
                            onAccepted: {
                                 fileField.text.text = fileDialog.fileUrl
                        //console.log(browseButton.y)
                                // You can perform further actions with the selected file URL
                            }
                            
                            onRejected: {
                                console.log(textFieldRectangle.width)
                            }
                        }
                        
                        TextField {
                            id: "fileField"
                            Layout.fillWidth: true
                            Text {
                                id: "text"
                                text: "Select Folder"
                                font.pixelSize: fileField.height / 2.5
                                topPadding: fileField.height / 4
                                leftPadding: 10
                            }
                            
                            width: addWorkspaceFrame.width * 0.6
                            height: browseButton.height
                            readOnly: true
                            
                            background: Rectangle {
                                radius: 10
                                border.color: "#C9C9C9"
                                border.width: 1
                            }
                        } 
                        
                        Button {
                            id: "browseButton"
                            anchors.left: fileField.right
                            anchors.leftMargin: 20
                            Layout.fillWidth: true
                            
                            contentItem: Text {
                                text: "Browse"
                                font.pixelSize: 20
                                horizontalAlignment: Text.AlignCentre
                                leftPadding: 5
                                topPadding: 5
                                bottomPadding: 5
                                rightPadding: 5
                            }
                            
                            onClicked: fileDialog.visible = true
                            
                            background: Rectangle {
                                radius: 5
                                border.color: "#C9C9C9"
                               
                                border.width: 1
                            }
                        }
                    }
                
            
    
    
    Rectangle{
        id:"lowerButtonsRectangle"
        x:24
        y:23
        
        anchors.top: textFieldRectangle.bottom
        anchors.topMargin:100

          
    Button {
        width: addWorkspaceFrame.width / 3
        id: "cancelButton"
        //anchors.topMargin: 10
        contentItem: Text {
            text: "Cancel"
            font.pixelSize: 20
           

             leftPadding: 100
            topPadding: 5
            bottomPadding: 5
            rightPadding: 50
        }
    }
    
    Button {
        width: addWorkspaceFrame.width / 3
        id: "saveButton"
        anchors.left: cancelButton.right
        anchors.leftMargin: 30
        contentItem: Text {
            text: "Save"
            font.pixelSize: 20
            horizontalAlignment: Text.AlignCentre
            leftPadding: 100
            topPadding: 5
            bottomPadding: 5
            rightPadding: 50
        }
    }}
    }
}
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFileDialog>
#include <QMessageBox>
#include <QStandardItem>
#include <iostream>
#include <QDirIterator>
#include <QCryptographicHash>
#include <QDateTime>
#include <QThread>
#include <QDebug>

MainWindow::MainWindow(QWidget *parent) :
  QMainWindow(parent),
  ui(new Ui::MainWindow)
{
  ui->setupUi(this);
  ui->PathText->setClearButtonEnabled(true);
  ui->progressBar->setRange(0,100);
  ui->progressBar->setValue(0);
  ui->nameChk->setChecked(true);
  ui->nameChk->setDisabled(true);
  ui->pathChk->setChecked(true);
  ui->pathChk->setDisabled(true);
  ui->sizeChk->setChecked(true);
  ui->sizeChk->setDisabled(true);
  ui->typeChk->setChecked(true);
  ui->typeChk->setDisabled(true);
  ui->tableWidget->resize(1920, 900);
  ui->tableWidget->show();
}

MainWindow::~MainWindow()
{
  delete ui;
}

int MainWindow::set_table_size()
{
  if(ui->md5Chk->isChecked() && !ui->timeChk->isChecked()) {
      ui->tableWidget->setRowCount(700);
      ui->tableWidget->setColumnCount(5);
      QStringList columnTitles;
      columnTitles << "Name" << "Path" << "Size" << "Type" << "Md5";
      ui->tableWidget->setHorizontalHeaderLabels(columnTitles);
      ui->tableWidget->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
      ui->tableWidget->horizontalHeader()->setSectionResizeMode(1,QHeaderView::ResizeToContents);
      ui->tableWidget->horizontalHeader()->setSectionResizeMode(4,QHeaderView::ResizeToContents);
      return 2;

   }else if(ui->timeChk->isChecked() && !ui->md5Chk->isChecked()) {
      ui->tableWidget->setRowCount(700);
      ui->tableWidget->setColumnCount(5);
      QStringList columnTitles;
      columnTitles << "Name" << "Path" << "Size" << "Type" << "Time";
      ui->tableWidget->setHorizontalHeaderLabels(columnTitles);
      ui->tableWidget->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
      ui->tableWidget->horizontalHeader()->setSectionResizeMode(1,QHeaderView::ResizeToContents);
      return 3;

  }else if(ui->md5Chk->isChecked() && ui->timeChk->isChecked()) {
      ui->tableWidget->setRowCount(700);
      ui->tableWidget->setColumnCount(6);
      QStringList columnTitles;
      columnTitles << "Name" << "Path" << "Size" << "Type" << "Time" << "Md5";
      ui->tableWidget->setHorizontalHeaderLabels(columnTitles);
      ui->tableWidget->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
      ui->tableWidget->horizontalHeader()->setSectionResizeMode(1,QHeaderView::ResizeToContents);
      return 4;

  }else{
      ui->tableWidget->setRowCount(700);
      ui->tableWidget->setColumnCount(4);
      QStringList columnTitles;
      columnTitles << "Name" << "Path" << "Size" << "Type";
      ui->tableWidget->setHorizontalHeaderLabels(columnTitles);
      ui->tableWidget->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
      ui->tableWidget->horizontalHeader()->setSectionResizeMode(1,QHeaderView::ResizeToContents);
      return 1;
  }
}

QString MainWindow::formatsize(qint64 size)
{
    QString new_size;
    if(size < 1024) {   //b
        new_size = QString::number(size).append("b");
        return new_size;
    }else if(size >= 1024 && size < 1048576) { //kb
        size /= 1024;
        new_size = QString::number(size).append("kb");
        return new_size;
    }else if(size > 1048576 && size < 1048576*1024) { //mb
        size /= 1024;
        size /= 1024;
        new_size =  QString::number(size).append("MB");
        return new_size;
      }else {
        size /= 1024;
        size /= 1024;
        size /= 1024;
        new_size =  QString::number(size).append("GB");
        return new_size;
      }

}

void MainWindow::on_selectBut_clicked()
{
    ui->PathText->clear();
    ui->tableWidget->clearContents();
    QString path = QFileDialog::getExistingDirectory(this, tr("Open Dir"), "/home/danny/Documents/");
    if(!path.isEmpty()) {
        ui->PathText->insert(path);
    }
}

void MainWindow::handle_update(QString md5, int count)
{
    int col_index = ui->tableWidget->columnCount() - 1;
    ui->tableWidget->setItem(count++,col_index,new QTableWidgetItem(md5));
    ui->progressBar->setValue(count);
    //qDebug("%d", count);
}

QString Md5Thread::getFileMd5(QString filePath)
{
    QFile localFile(filePath);

    if (!localFile.open(QFile::ReadOnly))
    {
        //QMessageBox::warning(this, "Warning", "Error in opening file", QMessageBox::Ok);
        return nullptr;
    }

    QCryptographicHash ch(QCryptographicHash::Md5);

    quint64 totalBytes = 0;
    quint64 bytesWritten = 0;
    quint64 bytesToWrite = 0;
    quint64 loadSize = 1024 * 4;
    QByteArray buf;

    totalBytes = quint64(localFile.size());
    bytesToWrite = quint64(totalBytes);

    while (1)
    {
        if(bytesToWrite > 0)
        {
            buf = QByteArray(localFile.read(long(qMin(bytesToWrite, loadSize))));
            ch.addData(buf);
            bytesWritten += quint64(buf.length());
            bytesToWrite -= quint64(buf.length());
            buf.resize(0);
        }
        else
        {
            break;
        }

        if(bytesWritten == totalBytes)
        {
            break;
        }
    }

    localFile.close();

    QString md5;
    md5 = ch.result().toHex();
    return md5;
}

void Md5Thread::run()
{
    QString md5;
    for(int i = 0; i < path_list.size(); ++i) {
        md5 = getFileMd5(path_list.at(i));
        emit update_info(md5, i);
    }
}

void MainWindow::startMd5Thread(QStringList path)
{
    Md5Thread *md5thread = new Md5Thread(this, path);
    connect(md5thread, SIGNAL(update_info(QString, int)), this, SLOT(handle_update(QString, int)));
    connect(md5thread, SIGNAL(finished()), md5thread, SLOT(deleteLater()));
    if(!md5thread->isRunning()) {
        md5thread->start();
    }
}

void MainWindow::browse_one(QString & path)
{
    int count = 0;
    QDirIterator iter(path, QDir::Files | QDir::CaseSensitive | QDir::NoDotAndDotDot, QDirIterator::Subdirectories);
    while(iter.hasNext()) {
        iter.next();
        QFileInfo file_info = iter.fileInfo();
        ui->tableWidget->setItem(count,0,new QTableWidgetItem(file_info.fileName()));
        ui->tableWidget->setItem(count,1,new QTableWidgetItem(file_info.absoluteFilePath()));
        ui->tableWidget->setItem(count,2,new QTableWidgetItem(formatsize(file_info.size())));
        ui->tableWidget->setItem(count++,3,new QTableWidgetItem(file_info.suffix()));
    }
}

void MainWindow::browse_two(QString & path)//need sync
{
  int count = 0;
  QStringList path_list;
  QDirIterator iter(path, QDir::Files | QDir::CaseSensitive | QDir::NoDotAndDotDot, QDirIterator::Subdirectories);
  while(iter.hasNext()) {
      iter.next();
      QFileInfo file_info = iter.fileInfo();
      path_list.append(file_info.absoluteFilePath());
      ui->tableWidget->setItem(count,0,new QTableWidgetItem(file_info.fileName()));
      ui->tableWidget->setItem(count,1,new QTableWidgetItem(file_info.absoluteFilePath()));
      ui->tableWidget->setItem(count,2,new QTableWidgetItem(formatsize(file_info.size())));
      ui->tableWidget->setItem(count++,3,new QTableWidgetItem(file_info.suffix()));
  }
  ui->progressBar->setRange(0, path_list.size());
  startMd5Thread(path_list);
}

void MainWindow::browse_three(QString & path)
{
    int count = 0;
    QDirIterator iter(path, QDir::Files | QDir::CaseSensitive | QDir::NoDotAndDotDot, QDirIterator::Subdirectories);
    while(iter.hasNext()) {
        iter.next();
        QFileInfo file_info = iter.fileInfo();
        ui->tableWidget->setItem(count,0,new QTableWidgetItem(file_info.fileName()));
        ui->tableWidget->setItem(count,1,new QTableWidgetItem(file_info.absoluteFilePath()));
        ui->tableWidget->setItem(count,2,new QTableWidgetItem(formatsize(file_info.size())));
        ui->tableWidget->setItem(count,3,new QTableWidgetItem(file_info.suffix()));
        ui->tableWidget->setItem(count++,4,new QTableWidgetItem(file_info.created().toString("yyyy-MM-dd hh:mm:ss")));
    }
}

void MainWindow::browse_four(QString & path)
{
    int count = 0;
    QStringList path_list;
    QDirIterator iter(path, QDir::Files | QDir::CaseSensitive | QDir::NoDotAndDotDot, QDirIterator::Subdirectories);
    while(iter.hasNext()) {
        iter.next();
        QFileInfo file_info = iter.fileInfo();
        path_list.append(file_info.absoluteFilePath());
        ui->tableWidget->setItem(count,0,new QTableWidgetItem(file_info.fileName()));
        ui->tableWidget->setItem(count,1,new QTableWidgetItem(file_info.absoluteFilePath()));
        ui->tableWidget->setItem(count,2,new QTableWidgetItem(formatsize(file_info.size())));
        ui->tableWidget->setItem(count,3,new QTableWidgetItem(file_info.suffix()));
        ui->tableWidget->setItem(count++,4,new QTableWidgetItem(file_info.created().toString("yyyy-MM-dd hh:mm:ss")));
    }
    ui->progressBar->setRange(0, path_list.size());
    startMd5Thread(path_list);
}

void MainWindow::on_confirmBut_clicked()
{
    int size_type;
    QString path = ui->PathText->text();
    QDir dir(path);
    if(path.isEmpty() || !dir.exists()) {
        QMessageBox::warning(this, "Warning", "Error in selecting path", QMessageBox::Ok);
    }
    size_type = set_table_size();
    qDebug() << "start";
    switch(size_type) {
        case 1:
            browse_one(path);
            break;
        case 2:
            browse_two(path);
            break;
        case 3:
            browse_three(path);
            break;
        case 4:
            browse_four(path);
            break;
        default:
            QMessageBox::warning(this, "Warning", "Error in selecting type", QMessageBox::Ok);
    }
}




















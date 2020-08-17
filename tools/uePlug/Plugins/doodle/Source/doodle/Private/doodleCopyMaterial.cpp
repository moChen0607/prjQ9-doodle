#include "doodleCopyMaterial.h"

#include "Editor/ContentBrowser/Public/ContentBrowserModule.h"
#include "Editor/ContentBrowser/Public/IContentBrowserSingleton.h"
#include "EditorAssetLibrary.h"

void DoodleCopyMat::Construct(const FArguments & Arg)
{
    //�����ue����Ĵ�������

    ChildSlot[
        SNew(SHorizontalBox)
            +SHorizontalBox::Slot()
            .AutoWidth()
            .HAlign(HAlign_Left)
            .Padding(FMargin(1.f,1.f))
            [
                SNew(SButton)//������ť
                .OnClicked(this, &DoodleCopyMat::getSelect)//��ӻص�����
                [
                    SNew(STextBlock).Text(FText::FromString("Get Select Obj"))//��ť�е��ַ�
                ]
            ]
            +SHorizontalBox::Slot( )
                .AutoWidth( )
                .HAlign(HAlign_Left)
                .Padding(FMargin(1.f, 1.f))
            [
                SNew(SButton)//������ť
                .OnClicked(this, &DoodleCopyMat::CopyMateral)//��ӻص�����
                [
                    SNew(STextBlock).Text(FText::FromString("copy To obj"))//��ť�е��ַ�
                ]
            ]
    ];
}

void DoodleCopyMat::AddReferencedObjects(FReferenceCollector& collector)
{
    //collector.AddReferencedObjects()
}

FReply DoodleCopyMat::getSelect( )
{
    /*
    ����ļ��������еĹǼ����������ѡ��
    ����һ����ť�Ļص�����
    */

    //����ļ���������ģ��(������?)
    FContentBrowserModule& contentBrowserModle = FModuleManager::Get( ).LoadModuleChecked<FContentBrowserModule>("ContentBrowser");
    TArray<FAssetData> selectedAss;
    contentBrowserModle.Get( ).GetSelectedAssets(selectedAss);
    for (int i = 0; i < selectedAss.Num( ); i++)
    {
        // ����ѡ�������Ƿ��ǹ�������
        if (selectedAss[i].GetClass( )->IsChildOf<USkeletalMesh>( ))
        {
            //����ǹ�������Ϳ��Ը��Ʋ�����
            UE_LOG(LogTemp, Log, TEXT("%s"), *(selectedAss[i].GetFullName( )));
            
            UObject* skinObj = selectedAss[i].ToSoftObjectPath( ).TryLoad( );// assLoad.LoadAsset(selectedAss[i].GetFullName( ));
            //�����ص���ת��ΪskeletalMesh�ಢ���д���
            copySoure = Cast<USkeletalMesh>(skinObj);
            UE_LOG(LogTemp, Log, TEXT("%s"), *(copySoure->GetPathName( )));
            //TArray<FSkeletalMaterial> SoureMat = copySoure->Materials;
            //for (int m = 0; m < SoureMat.Num( ); m++)
            //{
            //    SoureMat[m].MaterialInterface->GetPathName( );
            //    UE_LOG(LogTemp, Log, TEXT("%s"), *(SoureMat[m].MaterialInterface->GetPathName( )));
            //}

            //if (UClass *cl = skinObj->GetClass())
            //{
            //    if (UProperty *mproperty = cl->FindPropertyByName("materials"))
            //    {
            //        mproperty.
            //        UE_LOG(LogTemp, Log, TEXT("%s"), *(mproperty->GetName()));
            //    }
            //}
            //selectedAss[i].ToSoftObjectPath( ).TryLoad()
            //TFieldIterator<UProperty> iter(skinObj);
            //USkeletalMeshComponent test;
            //test.getmaterial
            //test.SetMaterial( );
            //UStaticMeshComponent test2;
            //test2.SetMaterial( );
        }
        //bool is =selectedAss[i].GetClass( )->IsChildOf<USkeletalMesh>( );
        //UE_LOG(LogTemp, Log, TEXT("%s"), *(FString::FromInt(is)));
        //selectedAss[i].GetFullName( )
    }
    return FReply::Handled( );
}

FReply DoodleCopyMat::CopyMateral( )
{
    FContentBrowserModule& contentBrowserModle = FModuleManager::Get( ).LoadModuleChecked<FContentBrowserModule>("ContentBrowser");
    TArray<FAssetData> selectedAss;
    contentBrowserModle.Get( ).GetSelectedAssets(selectedAss);
    for (int i = 0; i < selectedAss.Num( ); i++)
    {
        // ����ѡ�������Ƿ��ǹ�������
        if (selectedAss[i].GetClass( )->IsChildOf<USkeletalMesh>( ))
        {
            //����ǹ�������Ϳ��Ը��Ʋ�����
            UE_LOG(LogTemp, Log, TEXT("%s"), *(selectedAss[i].GetFullName( )));

            UObject* skinObj = selectedAss[i].ToSoftObjectPath( ).TryLoad( );// assLoad.LoadAsset(selectedAss[i].GetFullName( ));
            USkeletalMesh *copyTrange = Cast<USkeletalMesh>(skinObj);
            UE_LOG(LogTemp, Log, TEXT("%s"), *(copyTrange->GetPathName( )));
            TArray<FSkeletalMaterial> trangeMat = copyTrange->Materials;
            if (copySoure)
            {
                for (int m = 0; m < trangeMat.Num(); m++)
                {
                    trangeMat[m] = copySoure->Materials[m];
                    UE_LOG(LogTemp, Log, TEXT("%s"), *(trangeMat[m].MaterialInterface->GetPathName( )));
                }                       
            }
            copyTrange->Materials = trangeMat;
        }
    }
    return FReply::Handled( );
}

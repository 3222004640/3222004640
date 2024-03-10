#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#define  max_number  1024
//����ÿһ����������
size_t char_compare(char*org, size_t sum1, char*org_add, size_t sum2, size_t count)
{
	size_t i = 0, j = 0;
	while (i < sum1) {
		j = 0; // ����j���Ա�ÿ�δ�org_add�Ŀ�ʼ�����бȽ�  
		while (j < sum2) {
			if (org[i] == org_add[j]) {
				// �ҵ�ƥ����ַ�������count�������ڲ�ѭ��  
				if (org[i] != ' '&&org[i] != ','&&org[i] != ','&&org[i] != '!'&&org[i] != ':');
				count++;
				break;
			}
			j++; // ������org_add�в���  
		}
		i++; // �����Ƿ��ҵ�ƥ������������org�е���һ���ַ�  
	}
	return count; // 
}


int main(int argc,char*argv[])
{
	
	if (argc < 4) {
		printf("Usage: %s file1 file2\n", argv[0]);
		return 1;
	}
	FILE *fp = fopen(argv[1], "rb");
	if (fp == NULL)
	{
		printf("failed to open file1\n");
		return 0;
	}
	FILE *fp1 = fopen(argv[2], "rb");
	if (fp1 == NULL)
	{
		printf("failed to open file2\n");
		return 0;
	}
	//���ٶ�̬�ռ��������
	char *buffer1 = malloc(max_number * sizeof(char));
	char *buffer2 = malloc(max_number * sizeof(char));
	//�жϿռ��Ƿ�ɹ�
	if (buffer1 == NULL)
	{
		printf("ERROR\n");
		fclose(fp);
		fclose(fp1);
		return 0;
	}
	if (buffer2 == NULL)
	{
		printf("ERROR\n");
		fclose(fp);
		fclose(fp1);
		free(buffer1);
		return 0;
	}
	size_t size1, size2;//ÿһ������
	size_t Count = 0;//�ظ�����
	size_t total, total1, total2;//���ļ����������Ǹ����ļ�1�������ļ�2����
	total = 0; total1 = 0; total2 = 0;
	do {
		size1 = fread(buffer1, sizeof(char), max_number, fp);//���ļ������ݶ�ȡ����������
		size2 = fread(buffer2, sizeof(char), max_number, fp1);
		// �������������Ƚ��ַ�  
		Count = char_compare(buffer1, size1, buffer2, size2, Count);
		total1 += size1;
		total2 += size2;
	} while (size1 != 0 && size2 != 0);
	free(buffer1);
	free(buffer2);
	total = total1 > total2 ? total1 : total2;
	float similarity;//���ƶ�
	similarity = (float)Count / total;
	char buffer[50]; // ��洢С��ת��Ϊ�ַ�����Ľ��    
	snprintf(buffer, sizeof(buffer), "%0.2f", similarity);
	FILE *fp2 = fopen(argv[3], "w");
	if (fp2 == NULL)
	{
		printf("failed to open file3\n");
		return 0;
	}
	fputs(buffer, fp2);
	// �ͷſռ�
	fclose(fp);
	fclose(fp1);
	fclose(fp2);
	return 0;
}